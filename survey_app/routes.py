# routes.py

from flask import render_template, send_file
from survey_app import app
from survey_app.forms import RagForm, FreqForm, FreeTextForm
import sys

#sys.path.append('C:\\Users\\steve.baker\\PycharmProjects\\survey_platform\\survey_platform')
#import survey_platform as sp


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/rag', methods=['GET', 'POST'])
def rag():
    form = RagForm()
    if form.validate_on_submit():

        survey = sp.Survey(name='TESTSURVEY',
                           survey_type='SPECIALSURVEY',
                           questions_path='survey_app/static/questions.csv',
                           responses_path='survey_app/static/responses.parquet',
                           sample_path='survey_app/static/sample.parquet')

        return send_file(sp.get_rag(survey,
                                    seperator=form.trust.data,
                                    group_by=form.locality.data,
                                    questions=survey.questions),
                         as_attachment=True)

    return render_template('rag.html', form=form)


@app.route('/freetext', methods=['GET', 'POST'])
def text():
    form = FreeTextForm()
    if form.validate_on_submit():

        survey = sp.Survey(name='TESTSURVEY',
                           survey_type='SPECIALSURVEY',
                           questions_path='survey_app/static/questions.csv',
                           responses_path='survey_app/static/responses.parquet',
                           sample_path='survey_app/static/sample.parquet')

        return send_file(sp.get_freetext(combined=survey.combined.df,
                                    trust=form.trust.data,
                                    questions=survey.questions),
                         as_attachment=True)

    return render_template('freetext.html', form=form)


@app.route('/freq', methods=['GET', 'POST'])
def freq():
    form = FreqForm()
    if form.validate_on_submit():

        survey = sp.Survey(name='TESTSURVEY',
                           survey_type='SPECIALSURVEY',
                           questions_path='survey_app/static/questions.csv',
                           responses_path='survey_app/static/responses.parquet',
                           sample_path='survey_app/static/sample.parquet')

        return send_file(sp.get_freq_tables(combined=survey.combined.df,
                                    trust=form.trust.data,
                                    questions=survey.questions),
                         as_attachment=True)

    return render_template('freq.html', form=form)
