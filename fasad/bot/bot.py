import httpx
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command, StateFilter
from aiogram import Router
from aiogram.types import FSInputFile
from .markups import (
    get_main_keyboard,
    get_feedback_keyboard,
    get_phone_keyboard,
    get_comment_keyboard,
)
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.memory import MemoryStorage
from fasad.database.models import (session, Contact, Information, Session)



API_TOKEN = session.query(Information).filter(Information.name == "Токен бота").first().data
CHAT_ID = session.query(Information).filter(Information.name == "ID ТГ-админ чата").first().data

bot = Bot(token=API_TOKEN)
router = Router()
storage = MemoryStorage()
dp = Dispatcher(storage=storage)
dp.include_router(router)


class Form(StatesGroup):
    name = State()
    phone = State()
    comments = State()


# Обработчик команды /start
@dp.message(Command("start"))
async def send_welcome(message: types.Message):
    try:
        text = """
    Привет, узнай сегодня немного больше для решения своего вопроса:
        - Узнать больше о Facade Continent
        - Узнай больше о наших услугах 
        - Узнай как с нами связаться
        - Оставь заявку и мы сами свяжемся
        
    Дом мечты проще чем и ближе чем кажется!😊
        """
        await message.answer(text, reply_markup=get_main_keyboard())
    except Exception:
        await message.answer(
            "Извините, наверное произошла какая то неполадка, нужно попробовать немного позже.",
            reply_markup=get_main_keyboard(),
        )


# Обработчик нажатий на кнопки
@router.message()
async def handle_buttons(message: types.Message):
    try:
        if message.text == "О нас 🌟":
            text = """
    🌟 *Строительная компания Facade Continent* 🌟  
    *Более 18 лет на рынке!*
    
    Facade Continent – это строительная компания, которая с 2005 года занимается созданием загородных домов и превращением мечт в реальность. За это время мы не только стали важной частью строительной отрасли, но и завоевали доверие множества клиентов, которые выбрали нас для постройки своего идеального жилища. 🏡
    
    Мы понимаем, что фасад и кровля – это не просто защитные элементы вашего дома, но и ключевые аспекты его стиля и индивидуальности. Наша команда экспертов с большим вниманием подходит к каждому проекту, предлагая решения, которые сочетают в себе:
    
    - ✔️ *Качество*  
    - 🎨 *Эстетичность*  
    - ⏳ *Долговечность*  
    
    Все наши работы выполняются с использованием только лучших материалов, что гарантирует вам надежность и красоту на долгие годы.  
    
    Свяжитесь с нами и начните создание вашего идеального дома с Facade Continent! 😊
    """
            photo_path = "fasad/templates/image/image_with_logo.jpg"
            await message.reply_photo(photo=FSInputFile(photo_path), caption=text)

        elif message.text == "Наши услуги по фасаду 🏠":
            facade_services_message = """
            🌟 **Фасадные Работы** 🌟
                    
            🔨 **Наши услуги:**
    - Декоративная штукатурка: от 1000 руб/м²
    - Планкен: от 1500 руб/м²
    - Искусственный/натуральный камень: от 2500 руб/м²
    - Клинкерная плитка: от 2700 руб/м
    - Декор-элементы: от 400 руб/м.п.
    - Моделирующая декоративная штукатурка: от 1300 руб/м²
                    
            ✨ **Почему Мы?**
    - Качество и надежность
    - Команда профессионалов
    - Полный спектр услуг
    - Гарантия нашей работы
                    
            🔍 **И это еще не всё!** У нас есть множество других услуг, которые могут удовлетворить любые ваши потребности. Не стесняйтесь обращаться!
                    
            📞 **Свяжитесь с нами и создайте идеальный дом!** 😊                """
            photo_path = "fasad/templates/image/slide_facade_price/planken.jpg"
            await message.reply_photo(
                photo=FSInputFile(photo_path), caption=facade_services_message
            )
        elif message.text == "Наши услуги по кровле 🏠":
            roof_services_message = """
            🌟 **Кровельные Работы** 🌟
            
            🏠 **Наши услуги:**
    - Металлочерепица: от 2000 руб/м²
    - Цементно-песчаная черепица: от 2500 руб/м²
    - Гибкая черепица: от 2000 руб/м²
    - Модульная черепица: от 1900 руб/м²
    - Фальцевая кровля: от 2100 руб/м²
    - Керамическая черепица: от 2000 руб/м²
            
            ✨ **Почему Мы?**
    - Качество и надежность
    - Команда профессионалов
    - Полный спектр услуг
    - Гарантия нашей работы
    
    🔍 **И это еще не всё!** У нас есть множество других услуг, которые могут удовлетворить любые ваши потребности. Не стесняйтесь обращаться!
    
    📞 **Свяжитесь с нами и создайте идеальный дом!** 😊
                    """
            photo_path = "fasad/templates/image/slide_roof_price/cementno.jpg"
            await message.reply_photo(
                photo=FSInputFile(photo_path), caption=roof_services_message
            )
        elif message.text == "Связаться с нами 📱":
            phone = (
                session.query(Information).filter(Information.name == "Номер на сайте").first()
            )
            email = (
                session.query(Information).filter(Information.name == "Почта на сайте").first()
            )
            contact_message = f"""
            🌟 **Свяжитесь с Нами!** 🌟
    
            Мы всегда готовы ответить на ваши вопросы и помочь вам с вашим проектом! Не стесняйтесь обращаться – мы рады помочь!
    
            📞 **Телефон:**  
            {phone.data}
    
            📧 **Email:**  
            {email.data}
    
            Ваши идеи и пожелания для нас очень важны. Давайте вместе сделаем ваш проект успешным! 😊
            """
            photo_path = "fasad/templates/image/image_main/background.jpg"
            await message.reply_photo(
                photo=FSInputFile(photo_path), caption=contact_message
            )

    except Exception as e:
        print(e)
        await message.answer(
            "Извините, наверное произошла какая то неполадка, нужно попробовать немного позже.",
            reply_markup=get_main_keyboard(),
        )


@dp.message(lambda message: message.text == "Оставить заявку 📑")
async def start_feedback(message: types.Message, state: FSMContext):
    await state.set_state(Form.name)  # Устанавливаем состояние для имени
    user_name = message.from_user.first_name or "Гость"
    await message.answer(
        "Введите ваше имя или выберите опцию ниже:",
        reply_markup=get_feedback_keyboard(user_name),
    )


@dp.message(lambda message: message.text == "Использовать имя")
async def ask_phone(message: types.Message, state: FSMContext):
    await state.set_state(Form.phone)  # Устанавливаем состояние для телефона
    user_phone = "Неизвестный номер"
    await message.answer(
        "Введите ваш телефон или выберите опцию ниже:",
        reply_markup=get_phone_keyboard(user_phone),
    )


@dp.message(lambda message: message.text == "Отменить заявку")
async def cancel_feedback(message: types.Message, state: FSMContext):
    await state.clear()  # Завершаем состояние
    await message.answer(
        "Заявка отменена. Если у вас есть другие вопросы, просто напишите!",
        reply_markup=get_main_keyboard(),
    )


# Обработчик выбора имени
@dp.message(StateFilter(Form.name))
async def process_name(message: types.Message, state: FSMContext):
    try:
        if message.text.startswith("Использовать имя:"):
            name = message.from_user.first_name
        else:
            name = message.text

        await state.update_data(name=name)  # Сохраняем имя
        await state.set_state(Form.phone)  # Переходим к следующему состоянию
        await message.answer(
            "Введите ваш телефон :",
            reply_markup=get_phone_keyboard("Неизвестный номер"),
        )

    except Exception:
        await state.clear()  # Завершаем состояние
        await message.answer(
            "Извините, наверное произошла какая то неполадка, нужно попробовать немного позже.",
            reply_markup=get_main_keyboard(),
        )


@dp.message(StateFilter(Form.phone))
async def process_phone(message: types.Message, state: FSMContext):
    try:
        if message.text == "Пропустить телефон":
            phone = "Не указан"
        else:
            phone = message.text  # Сохраняем телефон

        await state.update_data(phone=phone)
        await state.set_state(Form.comments)  # Переходим к следующему состоянию
        await message.answer(
            "Введите комментарий:", reply_markup=get_comment_keyboard()
        )

    except Exception:
        await state.clear()  # Завершаем состояние
        await message.answer(
            "Извините, наверное произошла какая то неполадка, нужно попробовать немного позже.",
            reply_markup=get_main_keyboard(),
        )


@dp.message(StateFilter(Form.comments))
async def process_comments(message: types.Message, state: FSMContext):
    try:
        if message.text == "Пропустить комментарий":
            comments = "Нет комментариев"
        else:
            comments = message.text  # Сохраняем комментарий

        await state.update_data(comments=comments)

        # Получаем все данные
        data = await state.get_data()
        name = data.get("name")
        phone = data.get("phone")
        comments = data.get("comments")
        user_id = message.from_user.id
        username = message.from_user.username or "Не указано"
        session = Session()

        new = Contact(
            name=name,
            number_phone=phone or "None",
            question=comments,
            comments=comments,
        )
        session.add(new)
        session.commit()

        # Формируем сообщение
        message_text = (
            f"🔔 Получен запрос на Обратную связь 🔔\n"
            f"Данные пользователя:\n"
            f"👤 Запрос поступил с telegram: [@{username}](https://t.me/{username})\n"
            f"👤 ID: {user_id}\n"
            f"👤 NAME: {message.from_user.first_name}\n\n"
            f"Заполененные данные:\n"
            f"👩 Имя: {name}\n"
            f"📱 Телефон: {phone}\n"
            f"💬 Комментарии: {comments}"
        )
        # Отправляем сообщение в Telegram
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"https://api.telegram.org/bot{API_TOKEN}/sendMessage",
                json={"chat_id": CHAT_ID, "text": message_text},
            )

        # Проверка на успешность отправки сообщения
        if response.status_code == 200:
            await message.answer(
                "Спасибо! Ваша заявка отправлена.", reply_markup=get_main_keyboard()
            )
        else:
            await message.answer(
                "Извините, произошла ошибка при отправке заявки.",
                reply_markup=get_main_keyboard(),
            )

        await state.clear()  # Завершаем состояние

    except Exception:
        await state.clear()  # Завершаем состояние
        await message.answer(
            "Извините, наверное произошла какая то неполадка, нужно попробовать немного позже.",
            reply_markup=get_main_keyboard(),
        )


# Запуск бота
async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
