from fastapi import FastAPI
from database import Base, engine

# Создание таблиц в базе данных
Base.metadata.create_all(bind=engine)

app = FastAPI()

from api.comments_api import comments
from api.hashtag_api import hashtags
from api.posts_api import posts
from api.photo_api import photos
from api.users_api import users


@app.get('/hello')
async def hello():
    return {'hello': 'Fastapi'}


@app.post('/helloo')
async def post_home(name: str):
    return {'message': f'Hello {name}'}
