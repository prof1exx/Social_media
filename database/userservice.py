from database.models import User
from datetime import datetime

from database import get_db


# Регистрация пользователя
def register_user_db(name, email, phone_number, password, user_city):
    db = next(get_db())

    new_user = User(name=name, email=email, phone_number=phone_number,
                    password=password, user_city=user_city, reg_data=datetime.now())

    # Добавляем в базу
    db.add(new_user)
    # Сохраним в базе
    db.commit()

    return new_user.id


# Проверка на наличие в базе пользователя
def check_user_data_db(phone_number, email):
    db = next(get_db())

    # Проверка данных на наличие записи в базе
    checker = db.query(User).filter_by(phone_number=phone_number, email=email).first()

    # Если есть совпадения
    if checker:
        return False

    # Если нет совпадений
    return True


# Проверка пароля при входе в аккаунт
def check_user_password_db(email, password):
    db = next(get_db())

    # Попробуем найти пользователя
    checker = db.query(User).filter_by(email=email).first()

    # Если нашел такой мейл, проверяем правильность пароля
    if checker:
        # Начинаем сверку пароля
        if checker.password == password:
            return checker.id

        else:
            return 'Неверный пароль'

    # Если не находит данные в базе
    return 'Неверная почта'


# Получить информацию о пользователе
def profile_info_db(user_id):
    db = next(get_db())

    # Находим пользователя через id
    exact_user = db.query(User).filter_by(id=user_id).first()

    # Если нашел пользователя, передаю всю информацию про него
    if exact_user:
        return exact_user.email, \
            exact_user.phone_number, \
            exact_user.id, \
            exact_user.name, \
            exact_user.reg_date, \
            exact_user.user_city

    return 'Пользователь не найден'


# Изменение данных пользователя
def change_user_data(user_id, change_info, new_data):
    db = next(get_db())

    # Находим пользователя в базе
    exact_user = db.query(User).filter_by(id=user_id).first()
    db.delete(exact_user)
    db.commit()

    # Если есть пользователь в базе
    if exact_user:
        # Проверка того, какую информацию хочет изменить пользователь
        if change_info == 'email':
            exact_user.email = new_data

        elif change_info == 'number':
            exact_user.phone_number = new_data

        elif change_info == 'name':
            exact_user.name = new_data

        elif change_info == 'city':
            exact_user.user_city = new_data

        elif change_info == 'password':
            exact_user.password = new_data

        # Сохраняем изменения в базе
        db.commit()

        return 'Данные успешно изменены'

    # Если не находим в базе пользователя
    return 'Пользователь не найден'
