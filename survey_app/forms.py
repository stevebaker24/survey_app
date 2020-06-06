from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectMultipleField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    trust = StringField('Organisation ID', validators=[DataRequired()])
    locality = StringField('Breakdown', validators=[DataRequired()])
    score_type = SelectMultipleField('Score Type', choices=[('pos', 'Positive'), ('neu', 'Neutral'), ('neg', 'Negative')],
                                     validators=[DataRequired()])
    submit = SubmitField('Submit')
