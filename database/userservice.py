from database.models import User
from datetime import datetime

from database import get_db


def register_user_db(id, login, phone_number, password, nickname, gender, age, city):
    db = next(get_db())

    new_user = User(id=id, login=login, phone_number=phone_number, password=password,
                    nickname=nickname, gender=gender, age=age, city=city, reg_date=datetime.now())

    db.add(new_user)
    db.commit()

    return new_user.id


def check_user_data_db(phone_number, login):
    db = next(get_db())

    checker = db.query(User).filter_by(phone_number=phone_number, login=login).first()

    if checker:
        return False

    return True


def check_user_password_db(login, password):
    db = next(get_db())

    checker = db.query(User).filter_by(email=login).first()

    if checker:
        if checker.password == password:
            return checker.id

        else:
            return 'Неверный пароль'

    return 'Неверная почта'


def profile_info_db(user_id):
    db = next(get_db())

    exact_user = db.query(User).filter_by(id=user_id).first()

    if exact_user:
        return exact_user.id, \
            exact_user.login, \
            exact_user.phone_number, \
            exact_user.password, \
            exact_user.nickname, \
            exact_user.gender, \
            exact_user.age, \
            exact_user.city, \
            exact_user.reg_date

    return 'Пользователь не найден'


def change_user_data(user_id, change_info, new_data):
    db = next(get_db())

    exact_user = db.query(User).filter_by(id=user_id).first()
    db.delete(exact_user)
    db.commit()

    if exact_user:
        if change_info == 'id':
            exact_user.id = new_data

        elif change_info == 'login':
            exact_user.login = new_data

        elif change_info == 'phone_number':
            exact_user.phone_number = new_data

        elif change_info == 'password':
            exact_user.password = new_data

        elif change_info == 'nickname':
            exact_user.nickname = new_data

        elif change_info == 'gender':
            exact_user.nickname = new_data

        elif change_info == 'age':
            exact_user.nickname = new_data

        elif change_info == 'city':
            exact_user.city = new_data

        db.commit()

        return 'Данные успешно изменены'

    return 'Пользователь не найден'
