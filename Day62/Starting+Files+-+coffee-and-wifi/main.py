from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, ValidationError
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

cof = '☕️'
coffee_emoji = [cof, cof * 2, cof * 3, cof * 4, cof * 5]
wif = '💪'
wifi_emoji = [wif, wif * 2, wif * 3, wif * 4, wif * 5, '✘']
pow_ = '🔌'
power_emoji = [pow_, pow_ * 2, pow_ * 3, pow_ * 4, pow_ * 5]


def location_check(form, field):
    if 'http' not in field.data:
        raise ValidationError('Please enter a valid Google Map URL for the caffee.')


def open_close_check(form, field):
    if 'AM' not in field.data.upper() or 'PM' not in field.data.upper():
        raise ValidationError('Please enter a valid time value with AM/PM at the end, e.g. 3:00PM')


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location = StringField('Location of Cafe on Google Map', validators=[DataRequired(), location_check])
    open = StringField('Open time', validators=[DataRequired()])
    close = StringField('Close time', validators=[DataRequired()])
    coffee_rating = SelectField('Coffee Rating', choices=coffee_emoji, validators=[DataRequired()])
    wifi_strength = SelectField('Wifi Strength', choices=wifi_emoji, validators=[DataRequired()])
    power = SelectField('Refreshing power', choices=power_emoji, validators=[DataRequired()])
    submit = SubmitField('Submit')

# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
#e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        with open('cafe-data.csv', mode='a') as csv_file:
            csv_file.write(f'\n{form.cafe.data},')
            csv_file.write(f'{form.location.data},')
            csv_file.write(f'{form.open.data},')
            csv_file.write(f'{form.close.data},')
            csv_file.write(f'{form.coffee_rating.data},')
            csv_file.write(f'{form.wifi_strength.data},')
            csv_file.write(f'{form.power.data}')
        return redirect(url_for('cafes'))
    # Exercise:
    # Make the form write a new row into cafe-data.csv
    # with   if form.validate_on_submit()
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
