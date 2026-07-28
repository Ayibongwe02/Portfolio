# -----------------------------------------------------------------------------
# data.py — single source of truth for all portfolio content.
# Templates render from these structures; nothing project-specific is
# hardcoded in the HTML itself.
# -----------------------------------------------------------------------------

PROFILE = {
    "name": "Ayibongwe Ndhlovu",
    "role": "Data Scientist — End-to-End Data-Driven Applications",
    "degree": "BCom Honours, Information Systems — University of the Witwatersrand",
    "focus": "Data modeling, applied machine learning, forecasting",
    "builds": "Full-stack apps — pipeline to interface",
    "email": "ayibongwe.ndhlovu@outlook.com",
    "github": "Ayibongwe02",
    "github_url": "https://github.com/Ayibongwe02",
    "linkedin": "ayibongwe-ndhlovu",
    "linkedin_url": "https://www.linkedin.com/in/ayibongwe-ndhlovu-452143231/",
}

PROJECTS = [
    {
        "slug": "stokvel-forecasting",
        "accent": "amber",
        "status": "LIVE",
        "name": "Stokvel Forecasting Dashboard",
        "tagline": "Time-series forecasting for group savings",
        "description": (
            "A dashboard built for stokvels (community savings groups) that tracks "
            "member contributions, withdrawals, and balances, then forecasts where "
            "each member's balance is heading using Holt-Winters exponential "
            "smoothing and ARIMA, both fit live in the app. A model accuracy page "
            "backtests the two methods against held-out data for every member, and "
            "a regional view compares savings behaviour across groups."
        ),
        "problem": (
            "Stokvel organizers usually only have a running total per member, with "
            "no way to tell whether someone is on track or falling behind until a "
            "payout date arrives. That makes it hard to plan ahead or step in early "
            "if a member's contributions start slipping."
        ),
        "solution": (
            "The app fits a Holt-Winters and an ARIMA model to each member's own "
            "contribution history, live, rather than just plotting past totals. "
            "That turns a record of what already happened into a forward-looking "
            "balance projection with a confidence band, so a member trending below "
            "their usual pace shows up before the payout date, not after."
        ),
        "next": (
            "Could extend to automatic alerts when a member's forecasted balance "
            "drops below a set threshold, support for tracking several stokvels "
            "under one login, or a connection to real transaction data from "
            "banking or mobile money APIs in place of CSV uploads."
        ),
        "highlights": [
            "Live Holt-Winters and ARIMA forecasting per member, with a 95% confidence band",
            "Train/holdout backtesting (RMSE, MAE, MAPE) rather than static, pre-computed numbers",
            "Contribution and withdrawal patterns grounded in real NASASA/FinScope survey figures, "
            "including a traditional December lump-sum payout for each member",
            "Backtest validated end-to-end: every member's series fits Holt-Winters and ARIMA "
            "cleanly with non-trivial, real backtested RMSE",
            "Regional and category breakdowns of contribution and withdrawal patterns",
        ],
        "stack": ["Python", "Streamlit", "Plotly", "statsmodels", "pandas", "Docker"],
        "links": [
            {"label": "Launch app", "url": "https://stokvel-app-dashboard-9gwtqemp8bn4wugj5ptvqu.streamlit.app/", "primary": True},
        ],
    },
    {
        "slug": "churn-signal",
        "accent": "teal",
        "status": "LIVE",
        "name": "Churn Signal — Telco Customer Churn Dashboard",
        "tagline": "A live-trained churn classifier, not a static score",
        "description": (
            "An interactive dashboard that trains a random forest classifier on "
            "historical telecom customer data with known churn outcomes, then "
            "scores new customers uploaded by the user. Rather than displaying a "
            "pre-computed risk score, the model is trained and evaluated inside "
            "the app itself, with an 80/20 train-test split and reported accuracy "
            "and ROC-AUC."
        ),
        "problem": (
            "Providers need to know which customers are likely to leave before "
            "they leave, not after the fact. A fixed, pre-scored file also goes "
            "stale the moment customer behaviour shifts, since there is no model "
            "behind it to re-evaluate anything."
        ),
        "solution": (
            "A random forest is trained inside the app on historical customers "
            "whose outcome (churned or not) is already known, learning which "
            "combinations of tenure, contract type, and charges tend to precede "
            "churn. That trained model is then applied to new, unlabeled "
            "customers to produce a risk score, with its accuracy and ROC-AUC "
            "shown on the same page so the prediction can be checked rather than "
            "taken on faith."
        ),
        "next": (
            "Could grow into a system that retrains on a schedule as new data "
            "comes in, sends retention alerts to account managers for high-risk "
            "customers, or compares several model types side by side rather than "
            "a single random forest."
        ),
        "highlights": [
            "In-app model training with confusion matrix, ROC curve, and feature importances",
            "Training data modeled on the real IBM Telco Churn dataset's distributions and "
            "segment-level churn rates, not arbitrary values",
            "Validated live-trained model performance: 0.81 ROC-AUC, 77.6% accuracy on a held-out split",
            "Handles missing columns in uploaded data by filling in training-set medians or modes",
            "A high-risk leaderboard, segment analysis, and a live SQL explorer over predictions",
        ],
        "stack": ["Python", "Streamlit", "scikit-learn", "Plotly", "SQLite", "Docker"],
        "links": [
            {"label": "Launch app", "url": "https://churn-signal-prot0type.streamlit.app/", "primary": True},
        ],
    },
    {
        "slug": "cybersentinel",
        "accent": "red",
        "status": "LIVE",
        "name": "CyberSentinel — Threat Intelligence Dashboard",
        "tagline": "Live anomaly detection and traffic forecasting",
        "description": (
            "A security operations dashboard that forecasts network traffic "
            "volume and flags anomalous behaviour in real time. Traffic "
            "forecasting uses Holt-Winters and ARIMA models from statsmodels, and "
            "anomaly detection uses an Isolation Forest with an adjustable "
            "sensitivity slider, both computed live rather than read from a "
            "pre-generated snapshot. The underlying traffic data is modeled on "
            "the CICIDS2017 taxonomy from the Canadian Institute for "
            "Cybersecurity, with attacker IPs drawn from real malicious ranges "
            "and victim hosts mapped to the correct enterprise ports for their role."
        ),
        "problem": (
            "Security teams need to catch unusual traffic as it happens, not "
            "after reviewing a static report. Fixed rules-based flagging also "
            "tends to miss attack patterns it wasn't explicitly written to catch."
        ),
        "solution": (
            "Traffic volume is forecast live with Holt-Winters and ARIMA, so the "
            "app has a running expectation of what normal traffic looks like. An "
            "Isolation Forest is then applied to current events to flag the ones "
            "that don't fit the learned pattern, rather than checking events "
            "against a fixed list of known bad signatures, which is what lets it "
            "catch behaviour it hasn't been told about in advance."
        ),
        "next": (
            "Could extend to a live streaming data feed instead of CSV uploads, "
            "automatic alerting into tools like Slack or a ticketing system when "
            "anomalies are flagged, or an ensemble of several anomaly detection "
            "models instead of a single Isolation Forest."
        ),
        "highlights": [
            "Security posture overview: blocked payloads, active mitigations, anomaly rate",
            "Attack categories, IP ranges, and port mappings modeled on the CICIDS2017 taxonomy",
            "Isolation Forest tuned to a 12% contamination rate, validated to flag 60 anomalies "
            "(exactly 12%) for the Threat Hunting log",
            "Holt-Winters forecast trained on 78 points of trend + seasonality, holding backtested "
            "MAPE to roughly 3–5%, with a 95% confidence interval",
            "Threat hunting view with a live, filterable anomaly log and per-event risk scores",
        ],
        "stack": ["Python", "Streamlit", "scikit-learn", "statsmodels", "Plotly", "Docker"],
        "links": [
            {"label": "Launch app", "url": "https://cybersecurity-incident-threat-intelligence-dashboard-ss.streamlit.app/", "primary": True},
        ],
    },
    {
        "slug": "anvil-forger",
        "accent": "mixed",
        "status": "PROTOTYPE LIVE · PLATFORM IN REPO",
        "name": "Anvil Forger — No-Code ML Training Platform",
        "tagline": "Upload a dataset, walk away with a deployable model",
        "description": (
            "A collaborative web platform where a team uploads a CSV or a folder "
            "of labeled images and trains a classification, regression, or image "
            "model through a web UI — no notebook required. Built end-to-end: a "
            "Flask backend with team accounts and invite-code project sharing, "
            "SQLite persistence, model export as pickle, ONNX, or a "
            "dependency-free \"universal\" bundle, and a production Docker image "
            "shipped through a three-workflow GitHub Actions pipeline to both "
            "Docker Hub and GitHub Container Registry."
        ),
        "problem": (
            "Most teams that want to try machine learning either need someone to "
            "write training code for every new dataset, or end up with notebooks "
            "that never leave a laptop. There's rarely a shared place for a team "
            "to upload data, train a model together, and get something that "
            "plugs into another system afterward."
        ),
        "solution": (
            "Anvil Forger wraps scikit-learn training (tabular) and image "
            "classification behind a web UI, so uploading a CSV or a labeled "
            "image folder is enough to produce a trained, evaluated model. Teams "
            "share a project through an invite code, and once a model's trained "
            "it can be exported (pickle / ONNX / dependency-free) or served "
            "immediately over a REST endpoint — the output is something to plug "
            "into another system, not just a chart."
        ),
        "next": (
            "Could extend to hyperparameter search, model versioning with "
            "rollback, PostgreSQL for multi-server deployments in place of "
            "SQLite's single-writer setup, or a library of pre-trained starter "
            "models teams can fork."
        ),
        "highlights": [
            "Team accounts with invite-code project sharing, tabular + image classification "
            "training in one platform",
            "Model export as pickle, ONNX, or a dependency-free \"universal\" bundle — or serve "
            "predictions instantly over a REST API",
            "Production multi-stage Docker build (~924MB image): non-root user, dropped "
            "capabilities, no-new-privileges, health checks",
            "Three-workflow GitHub Actions CI/CD pipeline: automated tests + lint, build & push "
            "to Docker Hub, build & push to GHCR",
            "ONNX model import, so a model trained elsewhere can be brought into the same "
            "serving layer",
        ],
        "stack": ["Python", "Flask", "scikit-learn", "ONNX", "SQLite", "Docker", "GitHub Actions", "Gunicorn"],
        "links": [
            {"label": "Live platform", "url": "https://anvil-forger-1.onrender.com/login", "primary": True},
            {"label": "Source · GitHub", "url": "https://github.com/Ayibongwe02/Anvil-Forger", "primary": False},
            {"label": "Image · Docker Hub", "url": "https://hub.docker.com/r/ayibongwe02/anvil-v2", "primary": False},
        ],
    },
    {
        "slug": "qc-batch-dashboard",
        "accent": "amber",
        "status": "LIVE",
        "name": "QC Batch Dashboard — Defect Classifier",
        "tagline": "An animated batch-scoring app for a model trained in Anvil Forger",
        "description": (
            "An interactive Streamlit app that batch-scores a folder of product "
            "images against a defect classifier exported straight out of Anvil "
            "Forger, complete with a live scanning grid, animated KPI cards, "
            "class-distribution bars, and a flagged-for-review queue for "
            "low-confidence predictions. Ships with a bundled 16-image holdout "
            "set (never seen during training) so it runs and demos instantly "
            "with no upload required."
        ),
        "problem": (
            "A model that trains cleanly is only half the story — quality "
            "control teams need a way to actually run it against a batch of "
            "images and see, at a glance, what passed, what got flagged, and "
            "why, without opening a notebook or trusting a black-box score."
        ),
        "solution": (
            "The app takes the pickled model exported from Anvil Forger, walks "
            "an image batch through it, and renders each result live as it's "
            "scored — a colored border per thumbnail as it scans, a progress "
            "bar, and a results dashboard once the run finishes. A confidence "
            "threshold slider controls when a prediction gets routed to a "
            "flagged-for-review queue instead of trusted outright, so the "
            "model's uncertainty is visible rather than hidden behind a single "
            "pass/fail label."
        ),
        "next": (
            "Could extend to a live folder-watch mode instead of manual zip "
            "upload, or a Docker deployment alongside the Streamlit Community "
            "Cloud hosting it already has."
        ),
        "highlights": [
            "Live scanning grid — each thumbnail gets a colored pass/flag/error border as it's scored, in real time",
            "Adjustable confidence threshold routes low-confidence predictions to a flagged-for-review queue",
            "Bundled 16-image holdout demo set (8 clean, 8 scratched) never seen during training, so it runs with zero upload needed",
            "Accepts an arbitrary zip of images for inference — no class-labeled folder structure required",
            "Verified end-to-end with Streamlit's AppTest framework and a live server boot, both clean with zero exceptions",
        ],
        "stack": ["Python", "Streamlit", "scikit-learn", "Pillow"],
        "links": [
            {"label": "Launch app", "url": "https://qc-analytic-dashb0ard.streamlit.app/", "primary": True},
        ],
    },
]

SKILL_GROUPS = [
    {"title": "Languages", "tools": ["Python", "SQL"]},
    {"title": "Data & Modeling", "tools": ["pandas", "NumPy", "scikit-learn", "statsmodels", "ONNX"]},
    {"title": "App & Platform Dev", "tools": ["Streamlit", "Flask", "Plotly", "REST APIs", "SQLite"]},
    {"title": "Deployment & CI/CD", "tools": ["Docker", "GitHub Actions", "Docker Hub", "GHCR", "Git"]},
]

# tool -> which projects (by slug) actually use it — drives the cross-reference
# table on the Skills page instead of invented "proficiency" percentages.
def build_stack_matrix():
    tools = {}
    for p in PROJECTS:
        for tool in p["stack"]:
            tools.setdefault(tool, []).append(p["slug"])
    # order by how many projects use it, then alphabetically
    ordered = sorted(tools.items(), key=lambda kv: (-len(kv[1]), kv[0]))
    return ordered

STACK_MATRIX = build_stack_matrix()

TICKER_ITEMS = [
    {"html": "<b>0.81</b> ROC-AUC · 77.6% accuracy", "tag": "risk-live", "src": "CHURN SIGNAL"},
    {"html": "<b>12%</b> contamination · 60/500 flagged exactly", "tag": "risk-warn", "src": "CYBERSENTINEL"},
    {"html": "<b>~3–5%</b> backtested MAPE, 95% CI", "tag": "risk-amber", "src": "CYBERSENTINEL FORECAST"},
    {"html": "<b>95%</b> confidence band forecasting", "tag": "risk-live", "src": "STOKVEL"},
    {"html": "<b>924MB</b> production Docker image", "tag": "risk-amber", "src": "ANVIL FORGER"},
    {"html": "<b>3-workflow</b> CI/CD → Docker Hub + GHCR", "tag": "risk-live", "src": "ANVIL FORGER"},
    {"html": "<b>16-image</b> holdout set scored live, zero exceptions", "tag": "risk-live", "src": "QC BATCH DASHBOARD"},
    {"html": "Holt-Winters + ARIMA fit <b>live</b>, not pre-computed", "tag": "risk-live", "src": "ALL SYSTEMS"},
]

STATS = [
    {"value": 5, "suffix": "", "label": "Live systems shipped"},
    {"value": 0.81, "suffix": "", "label": "ROC-AUC, Churn Signal", "decimals": 2},
    {"value": 95, "suffix": "%", "label": "Forecast confidence interval"},
    {"value": 3, "suffix": "", "label": "CI/CD workflows, Anvil Forger"},
]

DELIVERABLES = [
    {
        "title": "Forecasting & time-series systems",
        "body": "Holt-Winters / ARIMA models with backtested RMSE, MAE, and MAPE — not just a line drawn forward.",
    },
    {
        "title": "Classification & risk scoring",
        "body": "Models trained and evaluated in front of the user — confusion matrix, ROC-AUC, feature importances included.",
    },
    {
        "title": "Anomaly & threat detection",
        "body": "Isolation Forest / unsupervised pipelines with tunable sensitivity, built to catch what fixed rules miss.",
    },
    {
        "title": "Full platforms, not prototypes",
        "body": "Multi-user auth, model export/serving, containerized with Docker, and shipped through a real CI/CD pipeline.",
    },
]


def get_project(slug):
    for p in PROJECTS:
        if p["slug"] == slug:
            return p
    return None


def get_prev_next(slug):
    slugs = [p["slug"] for p in PROJECTS]
    i = slugs.index(slug)
    prev_p = PROJECTS[i - 1] if i > 0 else PROJECTS[-1]
    next_p = PROJECTS[(i + 1) % len(PROJECTS)]
    return prev_p, next_p
