
# 🧠 Code Teaching Assistant

A full-stack web app powered by Large Language Models (LLMs) that explains code, assesses its complexity, and generates flowcharts — designed especially for beginners learning to program.

---

## 📦 Features

✅ Multi-language support (Python, JavaScript, C++)  
✅ Beginner-friendly, line-by-line code explanations  
✅ Code complexity assessment  
✅ Mermaid.js flowchart visualization  
✅ Export explanations to PDF and Markdown  
✅ Fully containerized using Docker & Docker Compose

---

## 🧰 Tech Stack

- **Frontend**: React + Tailwind CSS + Vite
- **Backend**: FastAPI + OpenAI/OpenRouter API
- **LLM**: GPT model via a4f.co
- **Visualization**: Mermaid.js
- **Deployment**: Docker + Docker Compose

---

## 🚀 Project Setup

### 📁 Folder Structure

```
llm-code-explainer/
├── backend/
│   ├── main.py
│   ├── flowchart.py
│   ├── explain.py
│   ├── complexity.py
│   ├── .env
│   ├── Dockerfile
│   └── requirements.txt
├── frontend/
│   ├── Dockerfile
│   ├── vite.config.js
│   ├── index.html
│   ├── package.json
│   └── src/
│       ├── App.jsx
│       └── main.jsx
├── docker-compose.yml
```

---

## ⚙️ Local Development

### 🔧 1. Clone the repo

```bash
git clone https://github.com/aryanmnit/LLM-Code-Explainer.git
cd LLM-Code-Explainer
```

### 🔧 2. Add your API key

Create a `.env` file inside the `backend/` folder:

```env
OPENAI_API_KEY=MY A4F API KEY
OPENAI_API_BASE="https://api.a4f.co/v1"
```

---

## 🐳 Running with Docker

### 📦 1. Build & start

```bash
docker compose up --build
```

### 🔍 2. App will be available at:

- Frontend: [http://localhost:3000](http://localhost:3000)
- Backend docs (Swagger): [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 🧪 Manual (Non-Docker) Run

### 🖥️ Backend (FastAPI)

```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload --port 8000
```

### 🎨 Frontend (React)

```bash
cd frontend
npm install
npm run dev
```

---

## 📄 Export & Extras

- 📝 Export explanation to **Markdown**
- 📥 Export explanation to **PDF**
- 🔁 Flowchart rendered via **Mermaid.js**

---

## 🧠 API Endpoints

- `POST /explain` → Code explanation
- `POST /complexity` → Complexity level
- `POST /flowchart` → Mermaid diagram

Request body:
```json
{
  "code": "your source code here",
  "language": "Python | JavaScript | C++"
}
```

---

## ✅ Example Test Case (C++)

```cpp
#include <iostream>
using namespace std;
int main() {
  int num;
  cin >> num;
  if (num % 2 == 0)
    cout << "Even";
  else
    cout << "Odd";
}
```

---

## 📦 Deployment (Optional)

Deploy using:
- [Render](https://render.com)

---

## 🙌 Acknowledgements

- [OpenRouter.ai](https://a4f.co)
- [FastAPI](https://fastapi.tiangolo.com/)
- [Mermaid.js](https://mermaid.js.org/)
- [TailwindCSS](https://tailwindcss.com/)
- [Vite](https://vitejs.dev/)
