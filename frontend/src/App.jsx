import { useEffect, useRef, useState } from 'react'
import axios from 'axios'
import mermaid from 'mermaid'
import html2pdf from 'html2pdf.js'
import { marked } from 'marked'
import DOMPurify from 'dompurify'

function App() {
  const [code, setCode] = useState('')
  const [language, setLanguage] = useState('Python')
  const [response, setResponse] = useState('')
  const [loading, setLoading] = useState(false)
  const [outputType, setOutputType] = useState('text')
  const diagramRef = useRef()

  const backendURL = 'http://localhost:8000'

  const handleRequest = async (endpoint) => {
    setLoading(true)
    setResponse('')
    setOutputType(endpoint)

    try {
      const res = await axios.post(`${backendURL}/${endpoint}`, { code, language })
      const keyMap = {
        explain: 'explanation',
        complexity: 'complexity',
        flowchart: 'flowchart'
      }
      const data = res.data[keyMap[endpoint]] || '❌ No response from backend'
      setResponse(data)
    } catch (error) {
      setResponse('❌ Error: ' + (error.response?.data?.detail || error.message))
    } finally {
      setLoading(false)
    }
  }

  const handleExportPDF = () => {
    const element = document.getElementById('output')
    html2pdf().from(element).save('explanation.pdf')
  }

  const handleExportMarkdown = () => {
    const blob = new Blob([response], { type: 'text/markdown' })
    const link = document.createElement('a')
    link.href = URL.createObjectURL(blob)
    link.download = 'explanation.md'
    link.click()
  }

  useEffect(() => {
  if (outputType === 'flowchart' && response && diagramRef.current) {
    const mermaidCode = response.replace(/```mermaid|```/g, '').trim()
    console.log('🐛 Mermaid code to render:', mermaidCode)

    const container = document.createElement('div')
    container.className = 'mermaid'
    container.innerHTML = mermaidCode  // ✅ THE FIX

    diagramRef.current.innerHTML = ''
    diagramRef.current.appendChild(container)

    try {
      mermaid.initialize({ startOnLoad: false })
      mermaid.init(undefined, container)
    } catch (err) {
      diagramRef.current.innerHTML = '❌ Mermaid render error: ' + err.message
    }
  }
}, [response, outputType])



  const renderOutput = () => {
    if (loading) return '⏳ Loading...'
    if (!response) return '🔍 Output will appear here'

    if (outputType === 'flowchart') {
      return (
        <div
          ref={diagramRef}
          className="bg-white border p-4 rounded mt-4 min-h-[120px]"
          style={{ overflowX: 'auto' }}
        ></div>
      )
    }

    if (outputType === 'explain' || outputType === 'complexity') {
      const safeHTML = DOMPurify.sanitize(marked.parse(response))
      return <div dangerouslySetInnerHTML={{ __html: safeHTML }} />
    }

    return <pre>{response}</pre>
  }

  return (
    <div className="min-h-screen bg-gray-100 p-6">
      <div className="max-w-4xl mx-auto bg-white shadow-lg rounded-2xl p-6 space-y-4">
        <h1 className="text-2xl font-bold text-center">🧠 Code Teaching Assistant</h1>

        <textarea
          className="w-full p-3 border rounded-md font-mono h-48"
          placeholder="Paste your code here..."
          value={code}
          onChange={(e) => setCode(e.target.value)}
        />

        <div className="flex justify-between items-center">
          <select
            className="border p-2 rounded-md"
            value={language}
            onChange={(e) => setLanguage(e.target.value)}
          >
            <option>Python</option>
            <option>JavaScript</option>
            <option>C++</option>
          </select>

          <div className="space-x-2">
            <button className="bg-blue-600 text-white px-4 py-2 rounded-xl" onClick={() => handleRequest('explain')}>
              🧠 Explain
            </button>
            <button className="bg-green-600 text-white px-4 py-2 rounded-xl" onClick={() => handleRequest('complexity')}>
              📊 Complexity
            </button>
            <button className="bg-purple-600 text-white px-4 py-2 rounded-xl" onClick={() => handleRequest('flowchart')}>
              🔁 Flowchart
            </button>
          </div>
        </div>

        <div id="output" className="bg-gray-50 border p-4 rounded-md font-mono whitespace-pre-wrap">
          {renderOutput()}
        </div>

        <div className="flex justify-end space-x-2">
          <button className="bg-gray-700 text-white px-4 py-2 rounded-xl" onClick={handleExportPDF}>
            📥 Export PDF
          </button>
          <button className="bg-gray-500 text-white px-4 py-2 rounded-xl" onClick={handleExportMarkdown}>
            📝 Export MD
          </button>
        </div>
      </div>
    </div>
  )
}

export default App
