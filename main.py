from flask import Flask, render_template, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = '1917'

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


class AccessForm(FlaskForm):
    astronaut_id = StringField('ID астронавта', validators=[DataRequired()])
    astronaut_password = PasswordField('Пароль астронавта', validators=[DataRequired()])
    captain_id = StringField('ID капитана', validators=[DataRequired()])
    captain_token = PasswordField('Токен капитана', validators=[DataRequired()])
    remember_access = BooleanField('Запомнить доступ')
    submit = SubmitField('Доступ')


@app.route('/access', methods=['GET', 'POST'])
def access():
    form = AccessForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('access.html', title='Доступ к системам', form=form)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
