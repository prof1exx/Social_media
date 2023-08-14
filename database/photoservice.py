from database import get_db
from database.models import PostPhoto


# Получить все или определенную фотографию
def get_all_or_exact_photo_db(photo_id, user_id):
    db = next(get_db())

    # Если нужны все фотографии определенного пользователя
    if user_id:
        exact_user_photos = db.query(PostPhoto).filter_by(user_id=user_id).all()

        return {'status': 1, 'message': exact_user_photos}

    # Если нужна определенная фотография
    elif photo_id:
        exact_photo = db.query(PostPhoto).filter_by(id=photo_id).first()

        return {'status': 1, 'message': exact_photo}

    else:
        all_photos = db.query(PostPhoto).all()

        return {'status': 1, 'message': all_photos}


# Изменить фото профиля
def change_photo_db(photo_id, new_photo_path):
    db = next(get_db())

    exact_photo = db.query(PostPhoto).filter_by(id=photo_id).first()

    if exact_photo:
        exact_photo.photo_path = new_photo_path
        db.commit()

        return True

    return False


# Удаление фотографии
def delete_photo_db(photo_id):
    db = next(get_db())

    exact_photo = db.query(PostPhoto).filter_by(id=photo_id).first()

    if exact_photo:
        db.delete(exact_photo)
        db.commit()

        return 'Фото удалено'

    return 'Фото не найдено'
