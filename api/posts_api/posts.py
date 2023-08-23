from api import app
from fastapi import Request
from database.postservice import get_all_or_exact_post_db, change_post_text_db, delete_exact_post_db


@app.get('/api/posts')
async def get_all_or_exact_post(post_id: int = 0):
    if post_id:
        exact_post = get_all_or_exact_post_db(post_id)
        return {'status': 1, 'message': exact_post}
    return {'status': 0, 'message': 'Ошибка'}


@app.put('/api/posts')
async def change_user_post(request: Request):
    data = await request.json()

    post_id = data.get('post_id')
    new_text = data.get('new_text')

    if post_id and new_text:
        change_post_text_db(post_id, new_text)

        return {'status': 1, 'message': 'Пост изменен'}
    return {'status': 0, 'message': 'Ошибка'}


@app.delete('/api/posts')
async def delete_user_post(request: Request):
    data = await request.json()

    post_id = data.get('post_id')
    if post_id:
        delete_exact_post_db(post_id)
        return {'status': 1, 'message': 'Пост удален'}
    return {'status': 0, 'message': 'Ошибка'}
