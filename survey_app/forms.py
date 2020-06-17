from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectMultipleField, SelectField
from wtforms.validators import DataRequired


class RagForm(FlaskForm):
    trust = StringField('Organisation ID', validators=[DataRequired()])
    locality = StringField('Breakdown', validators=[DataRequired()])
    score_type = SelectField('Score Type', choices=[('pos', 'Positive'), ('neu', 'Neutral'), ('neg', 'Negative')])
    submit = SubmitField('Submit')


class FreeTextForm(FlaskForm):
    trust = StringField('Organisation ID', validators=[DataRequired()])
    submit = SubmitField('Submit')


class FreqForm(FlaskForm):
    trust = StringField('Organisation ID', validators=[DataRequired()])
    submit = SubmitField('Submit')
