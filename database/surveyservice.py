from database.models import CommentOnSurvey, Survey
from database import get_db


def get_all_or_exact_survey_db(survey_id):
    db = next(get_db())

    if survey_id == 0:
        return db.query(Survey).all()

    return db.query(Survey).filter_by(id=survey_id).first()


def change_survey_text_db(survey_id, new_text):
    db = next(get_db())

    exact_survey = db.query(Survey).filter_by(id=survey_id).first()

    if exact_survey:
        exact_survey.text = new_text
        db.commit()

        return 'Текст коммента успешно обновлен'

    return 'Ошибка'


def delete_exact_survey_db(survey_id):
    db = next(get_db())

    exact_survey = db.query(Survey).filter_by(id=survey_id).first()

    if exact_survey:
        db.delete(exact_survey)
        db.commit()

        return 'Опросник успешно удален'

    return 'Ошибка'


def get_exact_survey_comments_db(post_id):
    db = next(get_db())

    exact_survey_comments = db.query(CommentOnSurvey).filter_by(id=post_id).first()

    if exact_survey_comments:
        return exact_survey_comments

    return []


def public_comment_db(survey_id, user_id, text, reg_date):
    db = next(get_db())

    new_comment = CommentOnSurvey(survey_id=survey_id, user_id=user_id, text=text, reg_date=reg_date)

    db.add(new_comment)
    db.commit()

    return "Комментарий успешно опубликован"


def change_exact_comment_db(comment_id, new_comment_text):
    db = next(get_db())

    exact_comment = db.query(CommentOnSurvey).filter_by(id=comment_id).first()

    if exact_comment:
        exact_comment.text = new_comment_text
        db.commit()
        return "Комментарий успешно обновлен"

    return 'Ошибка'


def delete_exact_comment_db(comment_id):
    db = next(get_db())

    exact_comment = db.query(CommentOnSurvey).filter_by(id=comment_id).first()

    if exact_comment:
        db.delete(exact_comment)
        db.commit()
        return "Комментарий успешно удален"

    return 'Ошибка'
