from fastapi import FastAPI
from database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

from api.comments_on_posts_api import comments
from api.hashtag_api import hashtags
from api.posts_api import posts
from api.photo_api import photos
from api.users_api import users

