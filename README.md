# Salary Engine API

REST API for Israeli civil service salary calculations (מנהלי grade type).
Built with FastAPI. Deploys to Render in ~3 minutes.

## Live endpoints (once deployed)

| Endpoint | Method | Description |
|---|---|---|
| `/` | GET | Health check |
| `/api/info` | GET | Engine status and loaded data |
| `/api/calculate` | POST | Calculate one worker's salary |
| `/api/batch` | POST | Upload a גולמי .xlsx, get results CSV |
| `/api/grades` | GET | All grade codes and base salaries |
| `/api/vatek/{years}` | GET | Seniority multiplier for N years |
| `/docs` | GET | Interactive Swagger UI (try it in browser) |

---

## Deploy to Render (free, ~3 minutes)

### Step 1 — Push to GitHub

```bash
# In this folder:
git init
git add .
git commit -m "initial salary engine API"

# Create a new repo on github.com, then:
git remote add origin https://github.com/YOUR_USERNAME/salary-engine.git
git push -u origin main
```

### Step 2 — Connect to Render

1. Go to [render.com](https://render.com) and sign up / log in with GitHub
2. Click **New → Web Service**
3. Select your `salary-engine` repository
4. Render auto-detects `render.yaml` — just click **Deploy**
5. Wait ~2 minutes for the build

Your API will be live at:
```
https://salary-engine.onrender.com
```

### Step 3 — Test it

Open `https://salary-engine.onrender.com/docs` in your browser.
You'll see the full interactive Swagger UI — try the `/api/calculate` endpoint directly.

Or with curl:
```bash
curl https://salary-engine.onrender.com/api/info
```

---

## Run locally (optional)

```bash
pip install -r requirements.txt
uvicorn main:app --reload
# Open http://localhost:8000/docs
```

---

## Project structure

```
salary_api/
├── main.py              # FastAPI app — all endpoints
├── requirements.txt     # Python dependencies
├── render.yaml          # Render deployment config
├── engine/
│   ├── lookups.py       # Grade (דרגה) and seniority (ותק) table loader
│   ├── calculator.py    # Single-worker salary calculation
│   └── batch.py         # Batch runner over גולמי Excel files
└── data/
    └── golmi.xlsx       # Reference data (grade + seniority lookup tables)
```

## API usage example

**Calculate one worker:**

```bash
curl -X POST https://salary-engine.onrender.com/api/calculate \
  -H "Content-Type: application/json" \
  -d '{
    "worker_id": 11021106,
    "ministry_code": 170,
    "ministry_name": "מכס ומע\"מ",
    "droog": 1,
    "job_pct": 1.0,
    "kod_darga": 202,
    "darga_label": "18",
    "vatek": 33.75,
    "components": [
      {"code": 10002, "name": "שכר משולב", "amount": 4158.5, "pensionable": "כן"},
      {"code": 4544,  "name": "3.6% ת. שכר", "amount": 228.77, "pensionable": "כן"}
    ]
  }'
```

**Batch verify a file:**

```bash
curl -X POST https://salary-engine.onrender.com/api/batch \
  -F "file=@path/to/golmi.xlsx" \
  -o results.csv
```
