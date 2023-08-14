from api import app
from database.postservice import (get_some_hashtags_db,
                                  get_exact_hashtag_db)


# Получить несколько хештегов
@app.get('/api/hashtag')
async def get_some_hashtags(size: int = 20, page: int = 1):
    pass


# Получить фото из определенного хештега
@app.get('/api/hashtag/<str:hashtag_name>')
async def get_exact_hashtag(hashtag_name: str):
    if hashtag_name:
        exact_hashtags = get_exact_hashtag_db(hashtag_name)

        return {'status': 1, 'message': exact_hashtags}

    return {'status': 0, 'message': 'No hashtag provided'}
