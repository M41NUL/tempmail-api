from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import httpx

app = FastAPI(
    title="Temp Mail API",
    description="Disposable email backend — by MAINUL - X",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

TEMP_MAIL = "https://api.internal.temp-mail.io/api/v3"


# ── HOME ──────────────────────────────────────────────
@app.get("/")
async def home():
    return {
        "status": "✅ Online",
        "owner": "MAINUL - X",
        "channel": "t.me/mdmainulislaminfo",
        "routes": {
            "GET  /generate":          "Generate new temp email",
            "GET  /inbox/{email}":     "Check inbox",
            "DELETE /delete/{email}":  "Delete email session",
        }
    }


# ── GENERATE ─────────────────────────────────────────
@app.get("/generate")
async def generate():
    async with httpx.AsyncClient(timeout=15) as client:
        resp = await client.post(
            f"{TEMP_MAIL}/email/new",
            json={"min_name_length": 10, "max_name_length": 10}
        )

    if resp.status_code != 200:
        raise HTTPException(502, "Temp Mail API error")

    data = resp.json()
    email = data.get("email")
    token = data.get("token")

    if not email:
        raise HTTPException(500, "Failed to generate email")

    return {
        "email": email,
        "token": token,
        "inbox_url": f"https://temp-mail.io/en/email/{email}/token/{token}"
    }


# ── INBOX ─────────────────────────────────────────────
@app.get("/inbox/{email}")
async def inbox(email: str):
    async with httpx.AsyncClient(timeout=15) as client:
        resp = await client.get(f"{TEMP_MAIL}/email/{email}/messages")

    if resp.status_code == 404:
        return {"messages": [], "count": 0}

    if resp.status_code != 200:
        raise HTTPException(502, "Failed to fetch inbox")

    messages = resp.json()

    clean = []
    for msg in messages:
        if not msg.get("from") and not msg.get("subject"):
            continue
        clean.append({
            "id":      msg.get("id"),
            "from":    msg.get("from", "Unknown"),
            "subject": msg.get("subject", "No Subject"),
            "body":    msg.get("body_text", ""),
            "date":    msg.get("created_at", ""),
        })

    return {"messages": clean, "count": len(clean)}


# ── DELETE ────────────────────────────────────────────
@app.delete("/delete/{email}")
async def delete(email: str):
    # Temp Mail API has no server-side delete; we just confirm cleared
    return {"success": True, "message": f"{email} session cleared"}
