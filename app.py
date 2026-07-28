from flask import Flask, render_template, abort

from data import (
    PROFILE,
    PROJECTS,
    SKILL_GROUPS,
    STACK_MATRIX,
    TICKER_ITEMS,
    STATS,
    DELIVERABLES,
    get_project,
    get_prev_next,
)

app = Flask(__name__)


@app.context_processor
def inject_globals():
    """Available in every template without passing explicitly."""
    return {"profile": PROFILE, "nav_projects": PROJECTS}


@app.route("/")
def home():
    return render_template(
        "home.html",
        active="home",
        projects=PROJECTS[:4],
        ticker_items=TICKER_ITEMS,
        stats=STATS,
    )


@app.route("/projects")
def projects():
    return render_template("projects.html", active="projects", projects=PROJECTS)


@app.route("/projects/<slug>")
def project_detail(slug):
    project = get_project(slug)
    if project is None:
        abort(404)
    prev_p, next_p = get_prev_next(slug)
    return render_template(
        "project_detail.html",
        active="projects",
        project=project,
        prev_project=prev_p,
        next_project=next_p,
    )


@app.route("/skills")
def skills():
    return render_template(
        "skills.html",
        active="skills",
        skill_groups=SKILL_GROUPS,
        stack_matrix=STACK_MATRIX,
        projects=PROJECTS,
    )


@app.route("/hire")
def hire():
    return render_template(
        "hire.html",
        active="hire",
        deliverables=DELIVERABLES,
    )


@app.errorhandler(404)
def not_found(e):
    return render_template("404.html"), 404


if __name__ == "__main__":
    app.run(debug=True, port=5050)
