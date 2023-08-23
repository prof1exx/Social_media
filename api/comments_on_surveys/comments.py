from api import app
from fastapi import Request
from database.surveyservice import get_exact_survey_comments_db, public_comment_db, \
    change_exact_comment_db, delete_exact_comment_db


@app.get('/api/comment_on_survey')
async def get_exact_survey_comments(request: Request):
    data = await request.json()

    survey_id = data.get('survey_id')

    if survey_id:
        exact_survey_comments = get_exact_survey_comments_db(survey_id)
        return {'status': 1, 'message': exact_survey_comments}
    return {'status': 0, 'message': 'Ошибка'}


@app.post('/api/comment_on_survey')
async def public_comment(request: Request):
    data = await request.json()

    survey_id = data.get('survey_id')
    user_id = data.get('user_id')
    text = data.get('text')
    reg_date = data.get('reg_date')

    if survey_id and user_id and text and reg_date:
        public_comment_db(survey_id, user_id, text, reg_date)

        return {'status': 1, 'message': 'Опросник опубликован'}
    return {'status': 0, 'message': 'Ошибка'}


@app.put('/api/comment_on_survey')
async def change_exact_user_comments(request: Request):
    data = await request.json()

    comment_id = data.get('comment_id')
    new_comment = data.get('new_comment_text')

    if comment_id and new_comment:
        change_exact_comment_db(comment_id, new_comment)

        return {'status': 1, 'message': 'Комментарий изменен'}
    return {'status': 0, 'message': 'Ошибка'}


@app.delete('api/comment_on_survey')
async def delete_exact_user_comment(request: Request):
    data = await request.json()

    comment_id = data.get('comment_id')

    if comment_id:
        delete_exact_comment_db(comment_id)
        return {'status': 1, 'message': 'Комментарий удален'}
    return {'status': 0, 'message': 'Ошибка'}
