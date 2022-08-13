from flask import Flask, render_template

import utils

# Запускаем приложение
app = Flask(__name__)


@app.route('/')
def index():
    candidates = utils.load_candidates_from_json()
    return render_template("list.html", candidates=candidates)


@app.route('/candidate/<int:id>')
def get_user(id):
    candidate = utils.get_candidate(id)
    return render_template("single.html", candidate=candidate)


@app.route('/search/<candidate_name>')
def get_name(candidate_name):
    candidates = utils.get_candidates_by_name(candidate_name)
    return render_template("search.html", candidates=candidates)


@app.route('/skills/<skill_name>')
def get_skills(skill_name):
    candidates = utils.get_candidates_by_skill(skill_name)
    return render_template("skill.html", skill=skill_name, candidates=candidates)


if __name__ == '__main__':
    app.run(port=5000)
