# Environment (.env) and Firebase JSON Setup

This guide shows exactly how to create the backend `.env` file and the Firebase service account `.json` file for this project.

Repo layout reference:

- Backend: `nexora-chat-bot-be/` (Flask API)
- Frontend: `nexora-chat-bot-fe/` (Vite/React)

The backend reads environment variables from `.env` via `python-dotenv` (see `nexora-chat-bot-be/config.py`) and expects a Firebase service key file at `nexora-chat-bot-be/firebase_key.json` (see `nexora-chat-bot-be/utils/firebase_config.py`).

---

## **1**) Create the .env file (backend)

Create a file named `.env` inside the backend folder: `nexora-chat-bot-be/.env`.

Recommended contents (replace placeholder values as needed):

```
# Flask Configuration
SECRET_KEY=change-me-to-a-long-random-string
FLASK_ENV=development

# Google API
GOOGLE_API_KEY=your-google-api-key

# File Upload
UPLOAD_FOLDER=uploads

# CORS Origins (comma-separated)
CORS_ORIGINS=http://localhost:5173
```

Notes
- `SECRET_KEY` is used by Flask; keep it secret.
- `GOOGLE_API_KEY` is read by the PDF/Chat utilities.
- `UPLOAD_FOLDER` defaults to `uploads` if not set.
- `CORS_ORIGINS` controls which frontends can talk to the API; add more origins separated by commas when needed (e.g., your deployed site URL).

Windows (PowerShell) quick create (optional):

```powershell
# Run from the repo root
New-Item -ItemType File -Path .\nexora-chat-bot-be\.env -Force | Out-Null
Set-Content -Path .\nexora-chat-bot-be\.env @"
# Flask Configuration
SECRET_KEY=change-me-to-a-long-random-string
FLASK_ENV=development

# Google API
GOOGLE_API_KEY=your-google-api-key

# File Upload
UPLOAD_FOLDER=uploads

# CORS Origins (comma-separated)
CORS_ORIGINS=http://localhost:5173
"@
```

If `python-dotenv` is not installed, install it in your backend environment so the `.env` file is loaded automatically by `config.py`:

```powershell
pip install python-dotenv
```

---

## 2) Create the Firebase service account JSON

Follow these steps to generate and place your Firebase Admin SDK key file.

### Step 2.1: Generate the service account key from Firebase

1. Open the [Firebase Console](https://console.firebase.google.com/) and select your project (e.g., `nexora-chat-bot`).
2. Go to: **Project Settings** (gear icon) → **Service Accounts** tab.
3. Click **"Generate new private key"** button.
4. Confirm the download – this will download a JSON file with a long auto-generated name like:
   - `nexora-chat-bot-firebase-adminsdk-xxxxx-1234567890.json`

### Step 2.2: Rename and place the file

5. **Rename** the downloaded file to: `firebase_key.json`
6. **Move** it into your backend folder:
   - `d:\3rd\back-end\Nexora_Chatbot\nexora-chat-bot-be\firebase_key.json`

### Step 2.3: Verify the JSON structure

Your `firebase_key.json` should look like this (with your actual values):

```json
{
  "type": "service_account",
  "project_id": "nexora-chat-bot",
  "private_key_id": "a41b42cd78e61b0b6c3f52d1e3471f0b47c5b9ac",
  "private_key": "-----BEGIN PRIVATE KEY-----\nYOUR_ACTUAL_PRIVATE_KEY_HERE\n-----END PRIVATE KEY-----\n",
  "client_email": "firebase-adminsdk-fbsvc@nexora-chat-bot.iam.gserviceaccount.com",
  "client_id": "101045524155641668709",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-xxxxx@nexora-chat-bot.iam.gserviceaccount.com",
  "universe_domain": "googleapis.com"
}
```

**Important fields:**
- `type`: Always "service_account"
- `project_id`: Your Firebase project ID (must match your project)
- `private_key`: The actual private key (keep this SECRET!)
- `client_email`: The service account email

### Why this exact name/path?

The backend initializes Firebase Admin here: `utils/firebase_config.py`
```python
cred = credentials.Certificate('firebase_key.json')
```
If you prefer a different filename/path, update that line accordingly.

### Security Warning

⚠️ **CRITICAL**: Do NOT commit this file to Git or share it publicly!
- The `private_key` field contains sensitive credentials
- Anyone with this file has full admin access to your Firebase project
- Add it to `.gitignore` immediately (see next section)

---

## **3**) .gitignore recommendations (security)

Ensure secrets are never pushed to Git. In the backend folder, create a `.gitignore` (or update a root one) and include:

```
# Backend secrets
nexora-chat-bot-be/.env
nexora-chat-bot-be/firebase_key.json
```

If you keep a backend-only `.gitignore`, the entries can be just:

```
.env
firebase_key.json
```

---

## **4**) Verifying your setup

- `.env` is loaded by `nexora-chat-bot-be/config.py` via `load_dotenv()`. You should see your settings reflected at runtime (e.g., CORS origin and upload folder behavior).
- `firebase_key.json` is read by `nexora-chat-bot-be/utils/firebase_config.py`. If the file is missing or invalid, the server will fail to initialize Firebase Admin.

Common checks
- CORS errors from the frontend: add your frontend URL to `CORS_ORIGINS` in `.env` (comma-separated) and restart the backend.
- “File not found: firebase_key.json”: confirm the file exists at `nexora-chat-bot-be/firebase_key.json` and the process has permission to read it.

---

## **5**) Optional alternative: environment variable path

If you prefer not to hardcode the filename in code, you can set an environment variable and change initialization code to use `applicationDefault()`:

```
GOOGLE_APPLICATION_CREDENTIALS=./nexora-chat-bot-be/firebase_key.json
```

Then update Firebase Admin init (optional pattern):

```python
import firebase_admin
from firebase_admin import credentials

cred = credentials.ApplicationDefault()
firebase_admin.initialize_app(cred)
```

This repo currently uses the explicit file path approach for simplicity; either pattern works.

---

## **6**)At a glance: what you now have

- `nexora-chat-bot-be/.env` with your Flask, Google API key, and CORS settings.
- `nexora-chat-bot-be/firebase_key.json` containing your Firebase service account credentials.
- Git ignored secrets to keep your keys safe.

You’re ready to run the backend and connect the frontend.


## How to launch

```bash
# Clone the repo
git clone https://github.com/your-org/nexora-campus-copilot.git
cd nexora-campus-copilot

# Install backend dependencies
cd backend
pip install -r requirements.txt
# Set environment variables
export GOOGLE_APPLICATION_CREDENTIALS="firebase_key.json"

# Run the backend
python app.py

# Install frontend dependencies
cd ../frontend
npm install
npm run dev
```


