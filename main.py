from fastapi import FastAPI
from database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

from api.comments_on_posts_api import comments
from api.comments_on_surveys import comments
from api.posts_api import posts
from api.surveys_api import surveys
from api.users_api import users
