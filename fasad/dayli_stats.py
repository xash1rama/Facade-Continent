from apscheduler.schedulers.background import BackgroundScheduler
from fastapi import APIRouter, Form
from starlette.responses import JSONResponse
import asyncio
from .database.models import Contact, session, Information
from .schemas.schemas import User
import httpx

router = APIRouter()


class Dayli:
    site_forms = 0
    telegram_forms = 0

    def site_pus(self):
        self.site_forms += 1

    def site_reset(self):
        self.site_forms = 0


today = Dayli()
unique_users = set()



@router.post("/contact_form")
async def receive_contact_form(
    name: str = Form(...),
    phone: str = Form(...),
    questions: str = Form(...),
    comments: str = Form(None),
):
    try:
        today.site_pus()
        new = Contact(name=name, number_phone=phone, question=questions, comments=comments)
        session.add(new)
        session.commit()

        # Формируем сообщение для бота
        message = (
            f"🔔Получен запрос с сайта на Обратную связь🔔\n\n"
            f"👩Имя: {name}\n"
            f"📱Телефон: {phone}\n"
            f"❓Вопрос: {questions}\n"
            f"💬Комментарии: {comments}"
        )

        # Отправляем сообщение в Telegram
        async with httpx.AsyncClient() as client:
            await client.post(
                f"https://api.telegram.org/bot7843457583:AAFF9sRfDL_otOjQfHMJEtIQhFXSN_e8T-4/sendMessage",
                json={"chat_id": -1002465218779, "text": message},
            )

        return {"status": "success", "message": "Данные успешно отправлены."}
    except Exception as er:
        async with httpx.AsyncClient() as client:
            error_type = str(type(er).__name__)
            error_message = str(er)
            message_text = f"""❗❗Прошу заметить❗❗️

На сервере произошла ошибка типа: 
{error_type}
**********

Ошибка говорит о следующем:
{error_message}

Ничего страшного не произошло, все работает в прежнем режиме✅
            """

            API_TOKEN = session.query(Information).filter(Information.name == "api_bot").first()
            CHAT_ID = session.query(Information).filter(Information.name == "group_tg_id").first()
            response = await client.post(
                f"https://api.telegram.org/bot{API_TOKEN.data}/sendMessage",
                json={"chat_id": CHAT_ID.data, "text": message_text},
            )




# Эндпоинт для обработки данных о пользователе
@router.post("/trackUser")
async def track_user(user: User):
    try:
        unique_users.add(user.user_id)
        return JSONResponse(
            status_code=200, content={"message": "User  tracked successfully"}
        )
    except Exception as er:
        async with httpx.AsyncClient() as client:
            error_type = str(type(er).__name__)
            error_message = str(er)
            message_text = f"""❗❗Прошу заметить❗❗️

        На сервере произошла ошибка типа: 
        {error_type}
        **********

        Ошибка говорит о следующем:
        {error_message}

        Ничего страшного не произошло, все работает в прежнем режиме✅
                    """

            API_TOKEN = session.query(Information).filter(Information.name == "api_bot").first()
            CHAT_ID = session.query(Information).filter(Information.name == "group_tg_id").first()
            response = await client.post(
                f"https://api.telegram.org/bot{API_TOKEN.data}/sendMessage",
                json={"chat_id": CHAT_ID.data, "text": message_text},
            )


# Функция для отправки отчетов
async def send_morning_report():

    unique_user_count = len(unique_users)
    two_st = "пользователя"
    one_st = "пользователь"
    more_st = "пользователей"
    aa = two_st
    if unique_user_count % 10 == 1:
        aa = one_st
    elif (unique_user_count % 10 == 0
          or unique_user_count % 10 == 5
          or unique_user_count % 10 == 6
          or unique_user_count % 10 == 7
          or unique_user_count % 10 == 8
          or unique_user_count % 10 == 9
    ):
        aa = more_st

    msg = f"""Доброe утро!😊
📊Время 8:30 - статистика📊 
🕕Статистика за посление 12 часов 🕕

👨Посещаемость сайта👨:
     {unique_user_count} {aa}
    
📄Заявок с сайта📄: {today.site_forms} 
 """

    API_TOKEN = session.query(Information).filter(Information.name == "api_bot").first()
    CHAT_ID = session.query(Information).filter(Information.name == "group_tg_id").first()
    # Отправляем сообщение в Telegram
    async with httpx.AsyncClient() as client:
        await client.post(
            f"https://api.telegram.org/bot{API_TOKEN.data}/sendMessage",
            json={"chat_id": CHAT_ID.data, "text": msg},
        )


async def send_evening_report():
    unique_user_count = len(unique_users)
    two_st = "пользователя"
    one_st = "пользователь"
    more_st = "пользователей"
    aa = two_st
    if unique_user_count % 10 == 1:
        aa = one_st
    elif (unique_user_count % 10 == 0
          or unique_user_count % 10 == 5
          or unique_user_count % 10 == 6
          or unique_user_count % 10 == 7
          or unique_user_count % 10 == 8
          or unique_user_count % 10 == 9
    ):
        aa = more_st

    msg = f"""Доброго Вечера! 😊
📊Время 20:30 - статистика📊 
🕕Статистика за посление 24 часа 🕕

👨Посещаемость сайта👨:
     {unique_user_count} {aa}

📄Заявок с сайта📄: {today.site_forms} 


🧹Обновляю статистику за сегодняшний день🧹
"""

    API_TOKEN = session.query(Information).filter(Information.name == "api_bot").first()
    CHAT_ID = session.query(Information).filter(Information.name == "group_tg_id").first()
    async with httpx.AsyncClient() as client:
        await client.post(
            f"https://api.telegram.org/bot{API_TOKEN.data}/sendMessage",
            json={"chat_id": CHAT_ID.data, "text": msg},
        )

    unique_users.clear()
    today.site_reset()


def schedule_reports():
    scheduler = BackgroundScheduler()
    scheduler.add_job(
        lambda: asyncio.run(send_morning_report()), "cron", hour=8, minute=30
    )  # Каждый день в 8:30
    scheduler.add_job(
        lambda: asyncio.run(send_evening_report()), "cron", hour=20, minute=30
    )  # Каждый день в 20:30
    scheduler.start()


schedule_reports()
