from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from summary import generate_daily_summary
from chat import chat_with_helper, save_chat
from flow import start_flow_timer, log_flow
from brain import generate_smart_brief, analyze_day

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/summary/daily")
def daily_summary():
    return {"summary": generate_daily_summary()}

@app.get("/api/flow/start")
def start_flow():
    return start_flow_timer()

@app.post("/api/flow/log")
async def log_flow_session(request: Request):
    data = await request.json()
    return log_flow(data.get("user_id", "anonymous"))

@app.post("/api/chat")
async def chat(request: Request):
    body = await request.json()
    user_message = body.get("message", "")
    return {"reply": chat_with_helper(user_message)}

@app.post("/api/chat/save")
async def save_chat_history(request: Request):
    body = await request.json()
    return save_chat(body)

@app.get("/api/ai/brain")
def brain():
    return generate_smart_brief()

@app.post("/api/ai/analyze-day")
async def analyze(request: Request):
    data = await request.json()
    return analyze_day(data)