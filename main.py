from flask import Flask, render_template

app = Flask(__name__)

PROFESSIONS = [
    "инженер-строитель",
    "пилот",
    "врач",
    "биолог",
    "геолог",
    "метеоролог",
    "агроном",
    "кибернетик",
    "энергетик",
    "психолог"
]


@app.route('/')
@app.route('/index')
@app.route('/index/<title>')
def index(title="Mars Colonization Mission"):
    return render_template('base.html', title=title)


@app.route('/training/<prof>')
def training(prof):
    return render_template('training.html', prof=prof.lower())


@app.route('/list_prof/<list_type>')
def list_prof(list_type):
    return render_template('list_prof.html',
                           list_type=list_type,
                           prof_list=PROFESSIONS)


@app.route('/answer')
@app.route('/auto_answer')
def auto_answer():
    form_data = {
        'title': 'Анкета участника миссии',
        'surname': 'Watny',
        'name': 'Mark',
        'education': 'Выше среднего',
        'profession': 'Штурман марсахода',
        'sex': 'male',
        'motivation': 'Всегда мечтал застрять на Марсе!',
        'ready': 'True'
    }
    return render_template('auto_answer.html', **form_data)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
