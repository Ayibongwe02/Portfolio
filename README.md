# Portfolio — Flask multi-page site

A multi-page portfolio built with Flask + Jinja templates, vanilla JS, and
hand-written CSS. Pages: Home, Projects (index), a case-study page per
project, Skills, and Hire/Contact.

## Run it locally

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

Open http://localhost:5050.

## Run with Docker

```bash
docker build -t portfolio .
docker run -d -p 8000:8000 portfolio
```

Open http://localhost:8000.

## Project structure

```
app.py                  Flask routes
data.py                 All project/skill/copy content — single source of truth
templates/              Jinja templates (base.html + one per page)
static/css/style.css    Design tokens + all animation
static/js/main.js       Page transitions, scroll reveal, tilt, ticker, counters
requirements.txt
Dockerfile
```

## Deploy it

Any host that runs a Flask app works — a few good free/cheap options:

- **Render** (render.com): connect the GitHub repo, set start command to
  `gunicorn app:app`, done.
- **Railway** (railway.app): connect the repo, it detects the Dockerfile
  automatically.
- **Fly.io**: `fly launch` in this folder, it will pick up the Dockerfile.
- **PythonAnywhere**: good free tier for a single Flask app if you want zero
  config beyond uploading the files.

To edit project content (add a project, tweak copy, update stack), everything
lives in `data.py` — the templates just render from it.
