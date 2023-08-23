from sqlalchemy import Column, DateTime, String, Integer, ForeignKey, BigInteger
from sqlalchemy.orm import relationship

from database import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(BigInteger, autoincrement=True, primary_key=True)
    login = Column(String, nullable=False)
    phone_number = Column(String, nullable=True)
    password = Column(String)

    nickname = Column(String, nullable=False)
    gender = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    city = Column(String, nullable=True)

    reg_date = Column(DateTime)


class Post(Base):
    __tablename__ = 'posts'

    id = Column(BigInteger, autoincrement=True, primary_key=True)
    user_id = Column(BigInteger, ForeignKey('user_posts.id'))

    label = Column(String, nullable=True)
    text = Column(String, nullable=True)

    reg_date = Column(DateTime)

    user_fk = relationship(User, lazy='subquery')


class Survey(Base):
    __tablename__ = 'surveys'

    id = Column(BigInteger, autoincrement=True, primary_key=True)
    user_id = Column(BigInteger, ForeignKey('user_posts.id'))

    choice1 = Column(String, nullable=True)
    choice2 = Column(String, nullable=True)
    choice3 = Column(String, nullable=True)
    choice4 = Column(String, nullable=True)

    reg_date = Column(DateTime)

    user_fk = relationship(User, lazy='subquery')


class CommentOnPost(Base):
    __tablename__ = 'comments_on_posts'

    id = Column(BigInteger, autoincrement=True, primary_key=True)
    post_id = Column(BigInteger, ForeignKey('user_posts.id'))
    user_id = Column(BigInteger, ForeignKey('users.id'))

    text = Column(String, nullable=False)

    reg_date = Column(DateTime)

    post_fk = relationship(Post, lazy='subquery')
    user_fk = relationship(User, lazy='subquery')


class CommentOnSurvey(Base):
    __tablename__ = 'comments_on_surveys'

    id = Column(BigInteger, autoincrement=True, primary_key=True)
    survey_id = Column(BigInteger, ForeignKey('user_posts.id'))
    user_id = Column(BigInteger, ForeignKey('users.id'))

    text = Column(String, nullable=False)

    reg_date = Column(DateTime)

    survey_fk = relationship(Survey, lazy='subquery')
    user_fk = relationship(User, lazy='subquery')
