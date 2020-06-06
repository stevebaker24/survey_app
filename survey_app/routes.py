# routes.py

from flask import render_template, send_file
from survey_app import app
from survey_app.forms import LoginForm
import sys

sys.path.append('C:\\Users\\steve.baker\\PycharmProjects\\survey_platform\\survey_platform')
import survey_platform as sp


@app.route('/', methods=['GET', 'POST'])
def index():
    form = LoginForm()
    if form.validate_on_submit():

        survey = sp.Survey('TESTSURVEY', 'SPECIALSURVEY', 'survey_app/static/questions.csv',
                           'survey_app/static/responses.parquet', 'survey_app/static/sample.parquet')

        return send_file(survey.combined.get_summary(form.trust.data, form.locality.data,
                                                     form.score_type.data), as_attachment=True)

    return render_template('index.html', form=form)
