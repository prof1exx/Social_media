from api import app
from fastapi import Request
from database.surveyservice import get_all_or_exact_survey_db, change_survey_text_db, delete_exact_comment_db


@app.get('/api/surveys')
async def get_all_or_exact_survey(survey_id: int = 0):
    if survey_id:
        exact_survey = get_all_or_exact_survey_db(survey_id)
        return {'status': 1, 'message': exact_survey}
    return {'status': 0, 'message': 'Ошибка'}


@app.put('/api/surveys')
async def change_user_survey(request: Request):
    data = await request.json()

    survey_id = data.get('survey_id')
    new_text = data.get('new_text')

    if survey_id and new_text:
        change_survey_text_db(survey_id, new_text)

        return {'status': 1, 'message': 'Пост изменен'}
    return {'status': 0, 'message': 'Ошибка'}


@app.delete('/api/surveys')
async def delete_user_survey(request: Request):
    data = await request.json()

    survey_id = data.get('survey_id')
    if survey_id:
        delete_exact_comment_db(survey_id)
        return {'status': 1, 'message': 'Пост удален'}
    return {'status': 0, 'message': 'Ошибка'}
