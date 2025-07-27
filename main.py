import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import smtplib
from email.message import EmailMessage
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow only devmohan.in and mohansagar.vercel.app
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://devmohan.in", "https://mohansagar.vercel.app"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class EmailRequest(BaseModel):
    to: str
    subject: str
    content: str

@app.post("/send-email")
async def send_email(request: EmailRequest):
    email_address = os.getenv("EMAIL_ADDRESS")
    email_password = os.getenv("EMAIL_PASSWORD")
    if not email_address or not email_password:
        raise HTTPException(status_code=500, detail="Email credentials not set.")
    msg = EmailMessage()
    msg["From"] = email_address
    msg["To"] = request.to
    msg["Subject"] = request.subject
    msg.set_content(request.content)
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(email_address, email_password)
            smtp.send_message(msg)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to send email: {str(e)}")
    return {"message": "Email sent successfully"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=10000)
