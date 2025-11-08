# RedSet ProtoCell Demo (Flask)

A minimal Flask demo that shows a Sniper/Spotter workflow. Uses simulated model responses by default so you can run without an API key.

## Files
- app.py
- sniper.py
- spotter.py
- prompt_bank.py
- templates/index.html
- static/style.css
- requirements.txt
- .env.local (template)
- .gitignore

## Quick start (macOS / Linux)
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
export FLASK_APP=app.py
export FLASK_ENV=development
flask run
```

## Quick start (Windows PowerShell)
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
$env:FLASK_APP = 'app.py'
$env:FLASK_ENV = 'development'
flask run
```

Open http://127.0.0.1:5000 in your browser.

To enable real OpenAI calls, install the `openai` package and add `OPENAI_API_KEY` to `.env.local`.
