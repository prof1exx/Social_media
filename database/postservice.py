from database.models import CommentOnPost, Post
from database import get_db


def get_all_or_exact_post_db(post_id):
    db = next(get_db())

    if post_id == 0:
        return db.query(Post).all()

    return db.query(Post).filter_by(id=post_id).first()


def change_post_text_db(post_id, new_text):
    db = next(get_db())

    exact_post = db.query(Post).filter_by(id=post_id).first()

    if exact_post:
        exact_post.text = new_text
        db.commit()

        return 'Текст коммента успешно обновлен'

    return 'Ошибка'


def delete_exact_post_db(post_id):
    db = next(get_db())

    exact_post = db.query(Post).filter_by(id=post_id).first()

    if exact_post:
        db.delete(exact_post)
        db.commit()

        return 'Пост успешно удален'

    return 'Ошибка'


def get_exact_post_comments_db(post_id):
    db = next(get_db())

    exact_post_comments = db.query(CommentOnPost).filter_by(id=post_id).first()

    if exact_post_comments:
        return exact_post_comments

    return []


def public_comment_db(post_id, user_id, text, reg_date):
    db = next(get_db())

    new_comment = CommentOnPost(post_id=post_id, user_id=user_id, text=text, reg_date=reg_date)

    db.add(new_comment)
    db.commit()

    return "Комментарий успешно опубликован"


def change_exact_comment_db(comment_id, new_comment_text):
    db = next(get_db())

    exact_comment = db.query(CommentOnPost).filter_by(id=comment_id).first()

    if exact_comment:
        exact_comment.text = new_comment_text
        db.commit()
        return "Комментарий успешно обновлен"

    return 'Ошибка'


def delete_exact_comment_db(comment_id):
    db = next(get_db())

    exact_comment = db.query(CommentOnPost).filter_by(id=comment_id).first()

    if exact_comment:
        db.delete(exact_comment)
        db.commit()
        return "Комментарий успешно удален"

    return 'Ошибка'
