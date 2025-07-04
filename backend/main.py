from dotenv import load_dotenv

load_dotenv()
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from explain import generate_explanation
from complexity import assess_complexity
from flowchart import generate_flowchart
from pydantic import BaseModel


app = FastAPI()

# CORS setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class CodeRequest(BaseModel):
    code: str
    language: str

@app.post("/explain")
def explain_code(request: CodeRequest):
    try:
        result = generate_explanation(request.code, request.language)
        return {"explanation": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/complexity")
def code_complexity(request: CodeRequest):
    try:
        result = assess_complexity(request.code, request.language)
        return {"complexity": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/flowchart")
def flowchart(request: CodeRequest):
    try:
        result = generate_flowchart(request.code, request.language)
        return {"flowchart": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
