from fastapi import Request
from pydantic import BaseModel
from typing import List, Dict

from database.userservice import (register_user_db,
                                  check_user_data_db,
                                  check_user_password_db,
                                  change_user_data,
                                  profile_info_db)

from api import app

# Проверка почты
import re

regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')


def mail_checker(email):
    if re.fullmatch(regex, email):
        return True
    else:
        return False


# Модель пользователя
class User(BaseModel):
    name: str
    email: str
    phone_number: str
    password: str
    user_city: str


# Регистрация пользователя
@app.post('/api/registration')
async def register_user(user_model: User):
    user_data = dict(user_model)
    # Валидация переданной почты
    mail_validation = mail_checker(user_model.email)

    # Если нет ошибок в почте
    if mail_validation:
        try:
            reg_user = register_user_db(**user_data)

            return {'status': 1, 'user_id': reg_user}

        except Exception as exc:
            return {'status': 0, 'message': exc}

    # Если ошибка в почте
    return {'status': 0, 'message': 'Invalid email'}


# Получить данные пользователя по user_id
@app.get('/api/user')
async def get_user(user_id: int):
    exact_user = profile_info_db(user_id)

    return {'status': 1, 'message': exact_user}


# Вход в аккаунт
@app.post('/api/login')
async def login_user(email: str, password: str):
    # Валидация переданной почты
    mail_validation = mail_checker(email)

    if mail_validation:
        login_checker = str(check_user_password_db(email, password))

        # Если все данные верны
        if login_checker.isdigit():
            return {'status': 1, 'user_id': int(login_checker)}

        return {'status': 1, 'message': login_checker}

    return {'status': 0, 'message': 'Invalid email'}


# Изменение данных о пользователе
@app.put('/api/change-profile')
async def change_user_profile(user_id: int, change_info: str, new_data: str):
    data = change_user_data(user_id, change_info, new_data)

    return {'status': 1, 'message': data}
