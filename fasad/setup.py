from contextlib import asynccontextmanager
from random import randint

from .main import FastAPI
from .database.models import (
    engine,
    Base,
    session,
    Information,
    Admin,
    FacadeStart,
    FacadeBase,
    FacadeFinish,
    RoofStart,
    RoofBase,
    RoofFinish,
)
from .config import API_KEY_BOT, ID_CHAT, PASSWORD, LOGIN


@asynccontextmanager
async def lifespan(main_app: FastAPI):
    Base.metadata.create_all(bind=engine)
    user = session.query(Admin).first()
    if user is None:
        create_datas()
    yield
    # Base.metadata.drop_all(bind=engine)


def create_datas():

    admin = Admin(login=LOGIN, password=PASSWORD)
    main_mail = Information(name="Почта на сайте", data="facadecontinent@gmail.com")
    main_phone = Information(name="Номер на сайте", data="+7(977)820-06-25")
    telegram = Information(name="Общая ТГ группа", data="https://t.me/+ObvZlEypYJU4MDcy")
    link_bot = Information(name="Ссылка на бота", data="https://t.me/AssistentFacadeBot")
    telegram_group_id = Information(name="ID ТГ-админ чата", data=ID_CHAT)
    api = Information(name="Токен бота", data=API_KEY_BOT)


    session.add(main_phone)
    session.add(main_mail)
    session.add(telegram)
    session.add(link_bot)
    session.add(admin)
    session.add(telegram_group_id)
    session.add(api)

    names_facade_start = [
        "Грунтовка стен",
        "Грунтовка откосов",
        "Утепление стен фасада",
        "Утепление откосов",
        "Армирование поверхности стен сеткой",
        "Армирование откосов",
        "Нанесение декоративной штукатурки",
    ]
    names_facade_base = [
        "Облицовка фасада искусственным декоративным камнем",
        "Укладка клинкерной плитки",
        "Гидрофобизация",
        "Монтаж откосов",
        "Шпатлевка откосов",
        "Установка подоконных отливов",
        "Деревянная обрешетка",
        "Монтаж планкена",
    ]
    names_facade_finish = [
        "Укладка клинкерной плитки",
        "Гидрофобизация",
        "Монтаж откосов",
        "Шпатлевка откосов",
        "Установка подоконных отливов",
        "Деревянная обрешетка",
        "Монтаж планкена",
    ]
    for i in names_facade_start:
        new = FacadeStart(name=i, price=randint(100,1000))
        session.add(new)

    for i in names_facade_base:
        new = FacadeBase(name=i, price=randint(100,1000))
        session.add(new)

    for i in names_facade_finish:
        new = FacadeFinish(name=i, price=randint(100,1000))
        session.add(new)

    names_roof_start = [
        "Монтаж кровли из металлочерепицы",
        "Монтаж кровли из модульной металлочерепицы",
        "Монтаж кровли из профнастила",
        "Монтаж кровли из композитной черепицы",
        "Монтаж гибкой черепицы",
        "Монтаж кровли из керамической черепицы",
        "Монтаж кровли из шифера",
        "Монтаж ондулина",
        "Монтаж фальцевой кровли",
        "Кровля из наплавляемых, рулонных материалов",
        "Монтаж кровли из профнастила",
    ]
    names_roof_base = [
        "Установка мауэрлата",
        "Установка стропильной системы",
        "Утепление крыши минватой",
        "Монтаж обрешетки",
        "Монтаж контробрешетки",
        "Сплошной настил из ОСП (OSB)",
        "Парогидроизоляция (мембраной, влаговетроизоляция)",
        "Обработка древесины огнебиозащитой",
        "Карнизных планок и капельников",
    ]
    names_roof_finish = [
        "Ветровых (фронтонных) планок",
        "Уплотнителей",
        "Проходов для вентиляции и канализации",
        "Трубчатых снегозадержателей",
        "Снегостопор",
        "Установка окна в готовую кровлю",
        "Демонтаж",
        "Разборка и сборка лесов",
    ]

    for i in names_roof_start:
        new = RoofStart(name=i, price=randint(100,1000))
        session.add(new)

    for i in names_roof_base:
        new = RoofBase(name=i, price=randint(100,1000))
        session.add(new)

    for i in names_roof_finish:
        new = RoofFinish(name=i, price=randint(100,1000))
        session.add(new)

    session.commit()

