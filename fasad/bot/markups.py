from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def get_main_keyboard() -> ReplyKeyboardMarkup:
    button_1 = KeyboardButton(text="О нас 🌟")
    button_2 = KeyboardButton(text="Наши услуги по фасаду 🏠")
    button_3 = KeyboardButton(text="Наши услуги по кровле 🏠")
    button_4 = KeyboardButton(text="Связаться с нами 📱")
    button_5 = KeyboardButton(text="Оставить заявку 📑")

    # Размещаем каждую кнопку в отдельной строке
    keyboard = ReplyKeyboardMarkup(
        keyboard=[[button_1], [button_2], [button_3], [button_4], [button_5]],
        resize_keyboard=True,
    )
    return keyboard


def get_feedback_keyboard(user_name: str) -> ReplyKeyboardMarkup:
    button_use_name = KeyboardButton(text=f"Использовать имя: {user_name}")
    button_skip = KeyboardButton(text="Отменить заявку")

    # Каждая кнопка в своей строке
    keyboard = ReplyKeyboardMarkup(
        keyboard=[[button_use_name], [button_skip]],
        resize_keyboard=True,
        one_time_keyboard=True,  # Клавиатура исчезнет после нажатия
    )

    return keyboard


def get_phone_keyboard(user_phone: str) -> ReplyKeyboardMarkup:
    # button_use_phone = KeyboardButton(text=f"Использовать номер: {user_phone}", request_contact=True)
    button_cancel = KeyboardButton(text="Отменить заявку")

    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            # [button_use_phone],
            [button_cancel]
        ],
        resize_keyboard=True,
        one_time_keyboard=True,
    )

    return keyboard


def get_comment_keyboard() -> ReplyKeyboardMarkup:
    button_roof = KeyboardButton(text="Вопрос по кровле")
    button_facade = KeyboardButton(text="Вопрос по фасаду")
    button_dabble = KeyboardButton(text="Вопрос и по кровле и по фасаду")
    button_skip_comment = KeyboardButton(text="Другой вопрос")
    button_cancel = KeyboardButton(text="Отменить заявку")

    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [button_roof],
            [button_facade],
            [button_dabble],
            [button_skip_comment],
            [button_cancel],
        ],
        resize_keyboard=True,
        one_time_keyboard=True,
    )

    return keyboard
