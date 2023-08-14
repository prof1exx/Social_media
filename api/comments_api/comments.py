from api import app
from fastapi import Request

from database.postservice import (get_exact_post_comments_db,
                                  public_comment_db,
                                  change_exact_comment_db,
                                  delete_exact_comment_db)


# Получить комментарии определенного поста
@app.get('/api/comment')
async def get_exact_post_comments(request: Request):
    # Получить JSON со всеми данными которые пришли из front
    data = await request.json()

    # Получить ключ post_id из data
    post_id = data.get('post_id')

    if post_id:
        # Получаем данные из базы
        exact_post_comments = get_exact_post_comments_db(post_id)

        return {'status': 1, 'message': exact_post_comments}

    return {'status': 0, 'message': 'неверный ввод данных'}


# Опубликовать комментарий к посту
@app.post('/api/comment')
async def public_comment():
    pass


# Изменить текст комментария
@app.put('/api/comment')
async def change_exact_user_comment():
    pass


# Удалить комментарий
@app.delete('/api/comment')
async def delete_exact_user_comment():
    pass
