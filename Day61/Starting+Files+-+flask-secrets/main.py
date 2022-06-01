from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, ValidationError
from flask_bootstrap import Bootstrap


app = Flask(__name__)
app.secret_key = 'asdf0123f-123sdflkj'
Bootstrap(app)


def length_check(form, field):
    if len(field.data) < 8:
        raise ValidationError('Field must be more than 8 characters')


def email_check(form, field):
    if '@' not in field.data:
        raise ValidationError('Invalid email address, please enter a valid one.')
    elif '.' not in field.data:
        raise ValidationError('Invalid email address, please enter a valid one.')


class LoginForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired(), email_check])
    password = PasswordField(label='Password', validators=[DataRequired(), length_check])
    submit = SubmitField(label='Log In')


@app.route("/")
def home():
    return render_template('index.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        correct_email = 'admin@email.com'
        correct_pass = '12345678'
        if form.email.data == correct_email and form.password.data == correct_pass:
            return render_template('success.html')
        return render_template('denied.html')
    return render_template('login.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)