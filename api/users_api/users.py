from pydantic import BaseModel

from database.userservice import (register_user_db,
                                  check_user_password_db,
                                  change_user_data,
                                  profile_info_db)

from api import app


# Модель пользователя
class User(BaseModel):
    id: str
    login: str
    phone_number: str
    password: str

    nickname: str
    gender: str
    age: str
    city: str


@app.post('/api/registration')
async def register_user(user_model: User):
    user_data = dict(user_model)

    try:
        reg_user = register_user_db(**user_data)

        return {'status': 1, 'user_id': reg_user}

    except Exception as exc:
        return {'status': 0, 'message': exc}


@app.get('/api/user')
async def get_user(user_id: int):
    exact_user = profile_info_db(user_id)

    return {'status': 1, 'message': exact_user}


@app.post('/api/login')
async def login_user(login: str, password: str):
    login_checker = str(check_user_password_db(login, password))

    if login_checker.isdigit():
        return {'status': 1, 'user_id': int(login_checker)}

    return {'status': 1, 'message': login_checker}


@app.put('/api/change-profile')
async def change_user_profile(user_id: int, change_info: str, new_data: str):
    data = change_user_data(user_id, change_info, new_data)

    return {'status': 1, 'message': data}
