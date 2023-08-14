from api import app
from fastapi import Request, Body, UploadFile

from database.photoservice import (get_all_or_exact_photo_db,
                                   change_photo_db,
                                   delete_photo_db)


# Получить все фотографии
@app.get('/api/photo')
async def get_all_or_exact_photo(photo_id: int = 0, user_id: int = 0):
    if photo_id and user_id:
        all_or_exact_photo = get_all_or_exact_photo_db(photo_id, user_id)

        return {'status': 1, 'message': all_or_exact_photo}

    return {'status': 0, 'message': 'неверный ввод данных'}


# Изменить фото профиля
@app.put('/api/photo')
async def change_user_photo(photo_id: int = Body(...),
                            photo_file: UploadFile = Body(...)):
    if photo_file:
        # Сохранить фото в папку
        with open(f'{photo_id}.jpg', 'wb') as photo:
            photo_to_save = await photo_file.read()
            photo.write(photo_to_save)

        change_photo_db(photo_id, f'/api/photo_api/photos/{photo_id}.jpg')

    return {'status': 1, 'message': 'Фото успешно изменено'}


# Удалить определенную фотографию
@app.delete('/api/photo')
async def delete_user_photo(request: Request):
    data = await request.json()
    post_id = data.get('post_id')

    if post_id:
        delete_photo = delete_photo_db(post_id)

        return {'status': 1, 'message': delete_photo}

    return {'status': 0, 'message': 'неверный ввод данных'}
