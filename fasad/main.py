import httpx
from fastapi import FastAPI, HTTPException, Request
from fastapi.templating import Jinja2Templates
from starlette.middleware.cors import CORSMiddleware
from starlette.middleware.sessions import SessionMiddleware
from starlette.staticfiles import StaticFiles
from starlette.responses import HTMLResponse
from .database.models import (
    FacadeStart,
    FacadeBase,
    FacadeFinish,
    Information,
    session,
    RoofStart,
    RoofBase,
    RoofFinish,
    PortfolioFacade,
    PhotoFacade,
    PhotoRoof,
    PortfolioRoof,
    desc
)
from .routes.route_admin import router as router_admin
from .routes.route_admin_portfolio import router as router_admin_portfolio
from .dayli_stats import router as router_contact
from .setup import lifespan
from .schemas.schemas import PortfolioResponse
import os
from typing import List
from prometheus_fastapi_instrumentator import Instrumentator
from .config import API_KEY_BOT as API_TOKEN, ID_CHAT as CHAT_ID


app = FastAPI(lifespan=lifespan)

instrumentator = Instrumentator()
instrumentator.instrument(app).expose(app)

app.include_router(router_contact)
app.include_router(router_admin)
app.include_router(router_admin_portfolio)


app.add_middleware(SessionMiddleware, secret_key="qwe1234567890")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(router_contact)
app.include_router(router_admin)
app.include_router(router_admin_portfolio)


app.mount("/image", StaticFiles(directory="fasad/templates/image"), name="image")
app.mount("/css", StaticFiles(directory="fasad/templates/css"), name="css")
app.mount("/scripts", StaticFiles(directory="fasad/templates/scripts"), name="scripts")


templates = Jinja2Templates(directory="fasad/templates")

PATH_IMAGE = os.path.join(os.getcwd(),"fasad", "templates", "image", "portfolio")


def get_api_token():
    token = session.query(Information).filter(Information.name == "Токен бота").first()
    return token.data

def get_id_group():
    token = session.query(Information).filter(Information.name == "ID ТГ-админ чата").first()
    return token.data

def get_number(num):
    number = ""
    for i in num:
        if i.isdigit():
            number += i
    return number


@app.exception_handler(404)  # Обработчик для 404 ошибок
async def not_found(request: Request, exc: HTTPException):
    informs = session.query(Information).all()
    email = session.query(Information).filter(Information.name == "Почта на сайте").first()
    phone = session.query(Information).filter(Information.name == "Номер на сайте").first()
    phone_main = get_number(phone.data)
    telegram = session.query(Information).filter(Information.name == "Общая ТГ группа").first()
    link_bot = session.query(Information).filter(Information.name == "Ссылка на бота").first()
    return templates.TemplateResponse(
        "error.html",
        {
            "request": request,
            "informs": informs,
            "phone": phone,
            "email": email,
            "phone_main": phone_main,
            "telegram": telegram,
            "link_bot": link_bot,
        },
        status_code=404,
    )


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    try:
        informs = session.query(Information).all()
        email = session.query(Information).filter(Information.name == "Почта на сайте").first()
        phone = session.query(Information).filter(Information.name == "Номер на сайте").first()
        phone_main = get_number(phone.data)
        telegram = session.query(Information).filter(Information.name == "Общая ТГ группа").first()
        link_bot = session.query(Information).filter(Information.name == "Ссылка на бота").first()
        return templates.TemplateResponse(
            "index.html",
            {
                "request": request,
                "informs": informs,
                "phone": phone,
                "email": email,
                "phone_main": phone_main,
                "telegram": telegram,
                "link_bot": link_bot,
            },
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

            response = await client.post(
                f"https://api.telegram.org/bot{get_api_token()}/sendMessage",
                json={"chat_id": get_id_group(), "text": message_text},
            )


@app.get("/service_facade", response_class=HTMLResponse)
async def service_facade(request: Request):
    try:
        facade_start = session.query(FacadeStart).all()
        facade_base = session.query(FacadeBase).all()
        facade_finish = session.query(FacadeFinish).all()

        informs = session.query(Information).all()
        email = session.query(Information).filter(Information.name == "Почта на сайте").first()
        phone = session.query(Information).filter(Information.name == "Номер на сайте").first()
        phone_main = get_number(phone.data)
        telegram = session.query(Information).filter(Information.name == "Общая ТГ группа").first()
        link_bot = session.query(Information).filter(Information.name == "Ссылка на бота").first()
        return templates.TemplateResponse(
            "service_facade.html",
            {
                "request": request,
                "facade_start": facade_start,
                "facade_base": facade_base,
                "facade_finish": facade_finish,
                "informs": informs,
                "phone": phone,
                "email": email,
                "phone_main": phone_main,
                "telegram": telegram,
                "link_bot": link_bot,
            },
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

            response = await client.post(
                f"https://api.telegram.org/bot{get_api_token()}/sendMessage",
                json={"chat_id": get_id_group(), "text": message_text},
            )


@app.get("/service_roof", response_class=HTMLResponse)
async def service_roof(request: Request):
    try:
        roof_start = session.query(RoofStart).all()
        roof_base = session.query(RoofBase).all()
        roof_finish = session.query(RoofFinish).all()

        informs = session.query(Information).all()
        email = session.query(Information).filter(Information.name == "Почта на сайте").first()
        phone = session.query(Information).filter(Information.name == "Номер на сайте").first()
        phone_main = get_number(phone.data)
        telegram = session.query(Information).filter(Information.name == "Общая ТГ группа").first()
        link_bot = session.query(Information).filter(Information.name == "Ссылка на бота").first()
        return templates.TemplateResponse(
            "service_roof.html",
            {
                "request": request,
                "roof_start": roof_start,
                "roof_base": roof_base,
                "roof_finish": roof_finish,
                "informs": informs,
                "phone": phone,
                "email": email,
                "phone_main": phone_main,
                "telegram": telegram,
                "link_bot": link_bot,
            },
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

            response = await client.post(
                f"https://api.telegram.org/bot{get_api_token()}/sendMessage",
                json={"chat_id": get_id_group(), "text": message_text},
            )


@app.get("/about", response_class=HTMLResponse)
async def about(request: Request):
    try:
        informs = session.query(Information).all()
        email = session.query(Information).filter(Information.name == "Почта на сайте").first()
        phone = session.query(Information).filter(Information.name == "Номер на сайте").first()
        phone_main = get_number(phone.data)
        telegram = session.query(Information).filter(Information.name == "Общая ТГ группа").first()
        link_bot = session.query(Information).filter(Information.name == "Ссылка на бота").first()
        return templates.TemplateResponse(
            "about.html",
            {
                "request": request,
                "informs": informs,
                "phone": phone,
                "email": email,
                "phone_main": phone_main,
                "telegram": telegram,
                "link_bot": link_bot,

            },
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

            response = await client.post(
                f"https://api.telegram.org/bot{get_api_token()}/sendMessage",
                json={"chat_id": get_id_group(), "text": message_text},
            )


@app.get("/contacts", response_class=HTMLResponse)
async def contacts(request: Request):
    try:
        informs = session.query(Information).all()
        email = session.query(Information).filter(Information.name == "Почта на сайте").first()
        phone = session.query(Information).filter(Information.name == "Номер на сайте").first()
        phone_main = get_number(phone.data)
        telegram = session.query(Information).filter(Information.name == "Общая ТГ группа").first()
        link_bot = session.query(Information).filter(Information.name == "Ссылка на бота").first()
        return templates.TemplateResponse(
            "contacts.html",
            {
                "request": request,
                "informs": informs,
                "phone": phone,
                "email": email,
                "phone_main": phone_main,
                "telegram": telegram,
                "link_bot": link_bot,
            },
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

            response = await client.post(
                f"https://api.telegram.org/bot{get_api_token()}/sendMessage",
                json={"chat_id": get_id_group(), "text": message_text},
            )


@app.get("/portfolio_facade", response_model=List[PortfolioResponse])
async def facade_portfolio(request: Request):
    try:
        portfolios = session.query(PortfolioFacade).order_by(desc(PortfolioFacade.id)).all()
        informs = session.query(Information).all()
        email = session.query(Information).filter(Information.name == "Почта на сайте").first()
        phone = session.query(Information).filter(Information.name == "Номер на сайте").first()
        phone_main = get_number(phone.data)
        telegram = session.query(Information).filter(Information.name == "Общая ТГ группа").first()
        link_bot = session.query(Information).filter(Information.name == "Ссылка на бота").first()
        portfolios_dict = {}
        for portfolio in portfolios:
            photos = (
                session.query(PhotoFacade.filename)
                .filter(PhotoFacade.portfolio_id == portfolio.id)
                .all()
            )
            portfolios_dict[portfolio.id] = {
                "main_photo": portfolio.main,
                "title": portfolio.title,
                "description": portfolio.description,
                "photos": photos,
            }
        return templates.TemplateResponse(
            "portfolio_facade.html",
            {
                "request": request,
                "portfolios": portfolios_dict,
                "informs": informs,
                "phone": phone,
                "email": email,
                "phone_main": phone_main,
                "telegram": telegram,
                "link_bot": link_bot,
            },
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

            response = await client.post(
                f"https://api.telegram.org/bot{get_api_token()}/sendMessage",
                json={"chat_id": get_id_group(), "text": message_text},
            )


@app.get("/portfolio_roof", response_model=List[PortfolioResponse])
async def roof_portfolio(request: Request):
    try:
        portfolios = session.query(PortfolioRoof).order_by(desc(PortfolioRoof.id)).all()
        informs = session.query(Information).all()
        email = session.query(Information).filter(Information.name == "Почта на сайте").first()
        phone = session.query(Information).filter(Information.name == "Номер на сайте").first()
        phone_main = get_number(phone.data)
        telegram = session.query(Information).filter(Information.name == "Общая ТГ группа").first()
        link_bot = session.query(Information).filter(Information.name == "Ссылка на бота").first()
        portfolios_dict = {}
        for portfolio in portfolios:
            photos = (
                session.query(PhotoRoof.filename)
                .filter(PhotoRoof.portfolio_id == portfolio.id)
                .all()
            )
            portfolios_dict[portfolio.id] = {
                "main_photo": portfolio.main,
                "title": portfolio.title,
                "description": portfolio.description,
                "photos": photos,
            }
        return templates.TemplateResponse(
            "portfolio_roof.html",
            {
                "request": request,
                "portfolios": portfolios_dict,
                "informs": informs,
                "phone": phone,
                "email": email,
                "phone_main": phone_main,
                "telegram": telegram,
                "link_bot": link_bot,
            },
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

            response = await client.post(
                f"https://api.telegram.org/bot{get_api_token()}/sendMessage",
                json={"chat_id": get_id_group(), "text": message_text},
            )
