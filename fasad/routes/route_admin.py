from fasad.database.models import (
    FacadeStart,
    FacadeBase,
    FacadeFinish,
    Information,
    RoofStart,
    RoofBase,
    RoofFinish,
    Admin,
    Contact,
    desc,
    session,
)
from fasad.schemas.schemas import GetString, NewData, Datas, DeleteData, UpdateFacade
import httpx
from fastapi import Depends, status, HTTPException, Request, APIRouter
from fastapi.security import HTTPBasicCredentials, HTTPBasic
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
templates = Jinja2Templates(directory="fasad/templates/admin")

router = APIRouter(tags=["admin"])
security = HTTPBasic()

def authenticate(credentials: HTTPBasicCredentials = Depends(security)):
    USERNAME = session.query(Admin.login).first()
    PASSWORD = session.query(Admin.password).first()

    if not USERNAME or not PASSWORD:
        raise HTTPException(status_code=500, detail="Ошибка базы данных")

    if credentials.username != USERNAME[0] or credentials.password != PASSWORD[0]:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Неверные учетные данные",
            headers={"WWW-Authenticate": "Basic"},
        )

    return credentials  # Возвращаем объект HTTPBasicCredentials


def get_number(num):
    number = ""
    for i in num:
        if i.isdigit():
            number += i
    return number
def get_api_token():
    token = session.query(Information).filter(Information.name == "Токен бота").first()
    return token.data

def get_id_group():
    token = session.query(Information).filter(Information.name == "ID ТГ-админ чата").first()
    return token.data


@router.get("/admin", response_class=HTMLResponse)
async def read_admin(
    request: Request, credentials: HTTPBasicCredentials = Depends(authenticate)
):
    try:
        facade_start = session.query(FacadeStart).all()
        facade_base = session.query(FacadeBase).all()
        facade_finish = session.query(FacadeFinish).all()

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
            "admin.html",
            {
                "request": request,
                "facade_start": facade_start,
                "facade_base": facade_base,
                "facade_finish": facade_finish,
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


@router.get("/logout")
async def logout(request: Request):
    try:
        request.session.clear()
        return RedirectResponse(url="/")
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


@router.get("/admin_prices_roof", response_class=HTMLResponse)
async def read_admin_price_roof(
    request: Request, credentials: HTTPBasicCredentials = Depends(authenticate)
):
    try:
        facade_start = session.query(FacadeStart).all()
        facade_base = session.query(FacadeBase).all()
        facade_finish = session.query(FacadeFinish).all()

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
            "admin_prices_roof.html",
            {
                "request": request,
                "facade_start": facade_start,
                "facade_base": facade_base,
                "facade_finish": facade_finish,
                "roof_start": roof_start,
                "roof_base": roof_base,
                "roof_finish": roof_finish,
                "informs": informs,
                "phone": phone,
                "email": email,
                "phone_main": phone_main,
                "telegram": telegram,
                "link_bot": link_bot
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


@router.get("/admin_prices_facade", response_class=HTMLResponse)
async def read_admin_price_facade(
    request: Request, credentials: HTTPBasicCredentials = Depends(authenticate)
):
    try:
        facade_start = session.query(FacadeStart).all()
        facade_base = session.query(FacadeBase).all()
        facade_finish = session.query(FacadeFinish).all()

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
            "admin_prices_facade.html",
            {
                "request": request,
                "facade_start": facade_start,
                "facade_base": facade_base,
                "facade_finish": facade_finish,
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


@router.get("/admin_portfolio_roof", response_class=HTMLResponse)
async def read_admin_portfolio_roof(
    request: Request, credentials: HTTPBasicCredentials = Depends(authenticate)
):
    try:
        informs = session.query(Information).all()
        email = session.query(Information).filter(Information.name == "Почта на сайте").first()
        phone = session.query(Information).filter(Information.name == "Номер на сайте").first()
        phone_main = get_number(phone.data)
        telegram = session.query(Information).filter(Information.name == "Общая ТГ группа").first()
        link_bot = session.query(Information).filter(Information.name == "Ссылка на бота").first()
        return templates.TemplateResponse(
            "admin_portfolio_roof.html",
            {
                "request": request,
                "informs": informs,
                "phone": phone,
                "email": email,
                "phone_main": phone_main,
                "telegram": telegram,
                "link_bot": link_bot
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


@router.post("/admin/create_data")
async def create_new_data(
    new_data: NewData, credentials: HTTPBasicCredentials = Depends(authenticate)
):
    try:
        new = Information(name=new_data.name, data=new_data.data)
        session.add(new)
        session.commit()
        return {"name": new_data.name, "data": new_data.data}
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


@router.put("/admin/data_update")
async def update_data(
    datas: Datas, credentials: HTTPBasicCredentials = Depends(authenticate)
):
    try:
        search = session.query(Information).filter(Information.id == datas.id).first()
        if search:
            search.name = datas.name
            search.data = datas.data
            session.commit()
            return {"name": datas.name, "data": datas.data}
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


@router.delete("/admin/data")
async def delete_data(
    id: DeleteData, credentials: HTTPBasicCredentials = Depends(authenticate)
):
    try:
        search = session.query(Information).filter(Information.id == id.id).first()
        if search:
            session.delete(search)
            session.commit()
            return {"id": id}
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


@router.post("/admin/create_start_facade")
async def create_new_facade(
    new_data: GetString, credentials: HTTPBasicCredentials = Depends(authenticate)
):
    try:
        new = FacadeStart(
            name=new_data.name, measure=new_data.measure, price=new_data.price
        )
        session.add(new)
        session.commit()
        return {
            "new_name": new_data.name,
            "new_measure": new_data.measure,
            "new_price": new_data.price,
        }
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


@router.put("/admin/start_facade_update")
async def update_facade(
    datas: UpdateFacade, credentials: HTTPBasicCredentials = Depends(authenticate)
):
    try:
        search = session.query(FacadeStart).filter(FacadeStart.id == datas.id).first()
        if search:
            search.name = datas.name
            search.measure = datas.measure
            search.price = datas.price
            session.commit()
            return {"status": "success"}  # Возвращаем статус и данные
        else:
            raise HTTPException(status_code=404, detail="Facade not found")
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


@router.delete("/admin/start_facade/{id}")
async def delete_start_facade(
    id: int, credentials: HTTPBasicCredentials = Depends(authenticate)
):
    try:
        search = session.query(FacadeStart).filter(FacadeStart.id == id).first()
        if search:
            session.delete(search)
            session.commit()
            return {"id": id}
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


@router.post("/admin/create_base_facade")
async def create_new_base_facade(
    new_data: GetString, credentials: HTTPBasicCredentials = Depends(authenticate)
):
    try:
        new = FacadeBase(
            name=new_data.name, measure=new_data.measure, price=new_data.price
        )
        session.add(new)
        session.commit()
        return {
            "new_name": new_data.name,
            "new_measure": new_data.measure,
            "new_price": new_data.price,
        }
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


@router.put("/admin/base_facade_update")
async def update_base_facade(
    datas: UpdateFacade, credentials: HTTPBasicCredentials = Depends(authenticate)
):
    try:
        search = session.query(FacadeBase).filter(FacadeBase.id == datas.id).first()
        if search:
            search.name = datas.name
            search.measure = datas.measure
            search.price = datas.price
            session.commit()
            return {"status": "success"}  # Возвращаем статус и данные
        else:
            raise HTTPException(status_code=404, detail="Facade not found")
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


@router.delete("/admin/base_facade/{id}")
async def delete_base_facade(
    id: int, credentials: HTTPBasicCredentials = Depends(authenticate)
):
    try:
        search = session.query(FacadeBase).filter(FacadeBase.id == id).first()
        if search:
            session.delete(search)
            session.commit()
            return {"id": id}
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


@router.post("/admin/create_finish_facade")
async def create_new_finish_facade(
    new_data: GetString, credentials: HTTPBasicCredentials = Depends(authenticate)
):
    try:
        new = FacadeFinish(
            name=new_data.name, measure=new_data.measure, price=new_data.price
        )
        session.add(new)
        session.commit()
        return {
            "new_name": new_data.name,
            "new_measure": new_data.measure,
            "new_price": new_data.price,
        }
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


@router.put("/admin/finish_facade_update")
async def update_finish_facade(
    datas: UpdateFacade, credentials: HTTPBasicCredentials = Depends(authenticate)
):
    try:
        search = session.query(FacadeFinish).filter(FacadeFinish.id == datas.id).first()
        if search:
            search.name = datas.name
            search.measure = datas.measure
            search.price = datas.price
            session.commit()
            return {"status": "success"}  # Возвращаем статус и данные
        else:
            raise HTTPException(status_code=404, detail="Facade not found")
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


@router.delete("/admin/finish_facade/{id}")
async def delete_finish_facade(
    id: int, credentials: HTTPBasicCredentials = Depends(authenticate)
):
    try:
        search = session.query(FacadeFinish).filter(FacadeFinish.id == id).first()
        if search:
            session.delete(search)
            session.commit()
            return {"id": id}
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


@router.post("/admin/create_start_roof")
async def create_new_start_roof(
    new_data: GetString, credentials: HTTPBasicCredentials = Depends(authenticate)
):
    try:
        new = RoofStart(
            name=new_data.name, measure=new_data.measure, price=new_data.price
        )
        session.add(new)
        session.commit()
        return {
            "new_name": new_data.name,
            "new_measure": new_data.measure,
            "new_price": new_data.price,
        }
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


@router.put("/admin/start_roof_update")
async def update_start_roof(
    datas: UpdateFacade, credentials: HTTPBasicCredentials = Depends(authenticate)
):
    try:
        search = session.query(RoofStart).filter(RoofStart.id == datas.id).first()
        if search:
            search.name = datas.name
            search.measure = datas.measure
            search.price = datas.price
            session.commit()
            return {"status": "success"}  # Возвращаем статус и данные
        else:
            raise HTTPException(status_code=404, detail="Facade not found")
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


@router.delete("/admin/start_roof/{id}")
async def delete_start_roof(
    id: int, credentials: HTTPBasicCredentials = Depends(authenticate)
):
    try:
        search = session.query(RoofStart).filter(RoofStart.id == id).first()
        if search:
            session.delete(search)
            session.commit()
            return {"id": id}
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


@router.post("/admin/create_base_roof")
async def create_new_base_roof(
    new_data: GetString, credentials: HTTPBasicCredentials = Depends(authenticate)
):
    try:
        new = RoofBase(
            name=new_data.name, measure=new_data.measure, price=new_data.price
        )
        session.add(new)
        session.commit()
        return {
            "new_name": new_data.name,
            "new_measure": new_data.measure,
            "new_price": new_data.price,
        }

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


@router.put("/admin/base_roof_update")
async def update_base_roof(
    datas: UpdateFacade, credentials: HTTPBasicCredentials = Depends(authenticate)
):
    try:
        search = session.query(RoofBase).filter(RoofBase.id == datas.id).first()
        if search:
            search.name = datas.name
            search.measure = datas.measure
            search.price = datas.price
            session.commit()
            return {"status": "success"}  # Возвращаем статус и данные
        else:
            raise HTTPException(status_code=404, detail="Facade not found")

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


@router.delete("/admin/base_roof/{id}")
async def delete_base_roof(
    id: int, credentials: HTTPBasicCredentials = Depends(authenticate)
):
    try:
        search = session.query(RoofBase).filter(RoofBase.id == id).first()
        if search:
            session.delete(search)
            session.commit()
            return {"id": id}

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


@router.post("/admin/create_finish_roof")
async def create_new_finish_roof(
    new_data: GetString, credentials: HTTPBasicCredentials = Depends(authenticate)
):
    try:
        new = RoofFinish(
            name=new_data.name, measure=new_data.measure, price=new_data.price
        )
        session.add(new)
        session.commit()
        return {
            "new_name": new_data.name,
            "new_measure": new_data.measure,
            "new_price": new_data.price,
        }

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


@router.put("/admin/finish_roof_update")
async def update_finish_roof(
    datas: UpdateFacade, credentials: HTTPBasicCredentials = Depends(authenticate)
):
    try:
        search = session.query(RoofFinish).filter(RoofFinish.id == datas.id).first()
        if search:
            search.name = datas.name
            search.measure = datas.measure
            search.price = datas.price
            session.commit()
            return {"status": "success"}  # Возвращаем статус и данные
        else:
            raise HTTPException(status_code=404, detail="Facade not found")
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


@router.delete("/admin/finish_roof/{id}")
async def delete_finish_roof(
    id: int, credentials: HTTPBasicCredentials = Depends(authenticate)
):
    try:
        search = session.query(RoofFinish).filter(RoofFinish.id == id).first()
        if search:
            session.delete(search)
            session.commit()
            return {"id": id}
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


@router.get("/admin_orders", response_class=HTMLResponse)
async def read_admin_orders(
    request: Request, credentials: HTTPBasicCredentials = Depends(authenticate)
):
    try:
        informs = session.query(Contact).order_by(desc(Contact.date)).all()
        email = session.query(Information).filter(Information.name == "Почта на сайте").first()
        phone = session.query(Information).filter(Information.name == "Номер на сайте").first()
        phone_main = get_number(phone.data)
        telegram = session.query(Information).filter(Information.name == "Общая ТГ группа").first()
        link_bot = session.query(Information).filter(Information.name == "Ссылка на бота").first()

        return templates.TemplateResponse(
            "admin_orders.html",
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


@router.delete("/admin_delete_order/{id}")
async def delete_order_(
    id: int, credentials: HTTPBasicCredentials = Depends(authenticate)
):
    try:
        search = session.query(Contact).filter(Contact.id == id).first()
        if search:
            session.delete(search)
            session.commit()
            return {"id": id}
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
