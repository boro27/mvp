import openai
import os
import json
from dotenv import load_dotenv
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_smart_brief():
    context = {
        "calendar_events": [
            "Deep work 10:00–12:00",
            "Client meeting 14:30",
            "Review 17:00"
        ],
        "flow_sessions": ["Yesterday: 90min", "Today: 30min"],
        "alerts": ["Back-to-back meetings", "No break scheduled"]
    }
    prompt = f"""You are HELPER AI.
Calendar: {context['calendar_events']}
Flow: {context['flow_sessions']}
Alerts: {context['alerts']}
Give a summary, risks, and improvements in JSON format (summary, suggestions[], risk_level)."""

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=500,
        temperature=0.7
    )
    try:
        return json.loads(response.choices[0].message.content)
    except Exception:
        return {"error": "Could not parse AI response."}

def analyze_day(data):
    prompt = f"""Analyze this daily input: {data}.
Give personalized productivity advice in JSON format."""
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=500,
        temperature=0.7
    )
    try:
        return json.loads(response.choices[0].message.content)
    except Exception:
        return {"error": "Could not parse AI response."}