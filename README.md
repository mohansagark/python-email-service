# Python Email Service API

A simple FastAPI-based service to send emails via Gmail SMTP.

## Features

- Exposes a single POST endpoint: `/send-email`
- Accepts JSON with `to`, `subject`, and `content` fields
- Uses Gmail SMTP (`smtp.gmail.com`, port 465) for sending emails
- Authenticates using environment variables: `EMAIL_ADDRESS` and `EMAIL_PASSWORD`

## Requirements

- Python 3.7+
- FastAPI
- Uvicorn

## Installation

```sh
pip install -r requirements.txt
```

## Usage

### Local Development

1. Set environment variables in your shell or `.env` file:
   - `EMAIL_ADDRESS`: Your Gmail address
   - `EMAIL_PASSWORD`: Your Gmail app password (see below)
2. Run the app:
   ```sh
   uvicorn main:app --host 0.0.0.0 --port 10000
   ```
3. Send a POST request to `http://localhost:10000/send-email`:
   ```sh
   curl -X POST http://localhost:10000/send-email \
     -H "Content-Type: application/json" \
     -d '{
       "to": "recipient@example.com",
       "subject": "Test Email",
       "content": "Hello from FastAPI!"
     }'
   ```

### Gmail App Password Setup

- Enable 2-Step Verification in your Google Account
- Go to Security > App Passwords
- Generate an app password for "Mail"
- Use your Gmail address and the app password for authentication

## Deployment (Render)

- Auto-deploy from GitHub on push
- Set `EMAIL_ADDRESS` and `EMAIL_PASSWORD` in Render's Environment Variables
- Use the start command:
  ```sh
  uvicorn main:app --host 0.0.0.0 --port 10000
  ```
- The endpoint will be available at: `https://<service-name>.onrender.com/send-email`

## Files

- `main.py`: FastAPI app
- `requirements.txt`: Dependencies
- `render.yaml`: Render deployment config
- `.gitignore`: Python ignores

## License

MIT
