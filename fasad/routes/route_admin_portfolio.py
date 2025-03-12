from fastapi import APIRouter, HTTPException, Form, UploadFile, File, Depends, Request
from fasad.database.models import (
    PhotoFacade,
    PhotoRoof,
    PortfolioRoof,
    PortfolioFacade,
    session,
    Information,
    desc,
)
from fastapi.security import HTTPBasicCredentials
from fasad.schemas.schemas import (
    PhotoResponse,
    PortfolioResponse,
)
from datetime import datetime
import os
import aiofiles
from typing import List
from fastapi.templating import Jinja2Templates
from starlette.responses import HTMLResponse

from .route_admin import get_number, authenticate, get_id_group, get_api_token
import httpx
from PIL import Image
import io

templates = Jinja2Templates(directory="fasad/templates/admin")
router = APIRouter(tags=["admin"])
PATH_IMAGE = os.path.join(os.getcwd(),"fasad", "templates", "image", "portfolio")


@router.get("/admin_portfolio_facade", response_class=HTMLResponse)
async def read_admin(
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
            "admin_portfolio_facade.html",
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


@router.get("/admin_portfolio_facade/{portfolio_id}", response_model=PortfolioResponse)
async def read_portfolio_facade(
    request: Request,
    portfolio_id: int,
    credentials: HTTPBasicCredentials = Depends(authenticate),
):
    try:
        portfolio = (
            session.query(PortfolioFacade)
            .filter(PortfolioFacade.id == portfolio_id)
            .first()
        )
        if not portfolio:
            raise HTTPException(status_code=404, detail="Портфолио не найдено")
        return PortfolioResponse(
            id=portfolio.id,
            title=portfolio.title,
            description=portfolio.description,
            main=portfolio.main,
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


@router.get("/admin_portfolio_facade_gallery", response_model=list[PortfolioResponse])
async def read_portfolios_facade(
    request: Request, credentials: HTTPBasicCredentials = Depends(authenticate)
):
    try:
        portfolios = session.query(PortfolioFacade).order_by(desc(PortfolioFacade.id)).all()
        return [
            PortfolioResponse(
                id=portfolio.id,
                title=portfolio.title,
                description=portfolio.description,
                main=portfolio.main,
            )
            for portfolio in portfolios
        ]
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


@router.put("/admin_portfolio_facade/{portfolio_id}", response_model=PortfolioResponse)
async def update_portfolio_facade(
    request: Request,
    portfolio_id: int,
    title: str = Form(...),
    description: str = Form(...),
    credentials: HTTPBasicCredentials = Depends(authenticate),
):
    try:
        portfolio_to_update = (
            session.query(PortfolioFacade)
            .filter(PortfolioFacade.id == portfolio_id)
            .first()
        )
        if not portfolio_to_update:
            raise HTTPException(status_code=404, detail="Портфолио не найдено")

        portfolio_to_update.title = title
        portfolio_to_update.description = description
        session.commit()
        return PortfolioResponse(
            id=portfolio_to_update.id,
            title=portfolio_to_update.title,
            description=portfolio_to_update.description,
            main=portfolio_to_update.main,
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


@router.put(
    "/admin_portfolio_facade/{portfolio_id}/main-image",
    response_model=PortfolioResponse,
)
async def update_main_image_facade(
    request: Request,
    portfolio_id: int,
    main: UploadFile = File(...),
    credentials: HTTPBasicCredentials = Depends(authenticate),
):
    try:
        print("Изменение главного изображения")

        portfolio = (
            session.query(PortfolioFacade)
            .filter(PortfolioFacade.id == portfolio_id)
            .first()
        )
        if not portfolio:
            return {"error": "Портфолио не найдено"}

        old_name = portfolio.main

        os.makedirs(PATH_IMAGE, exist_ok=True)
        contents = await main.read()
        file_name = f"{datetime.now()}_{main.filename}"
        file_path = os.path.join(PATH_IMAGE, file_name)
        async with aiofiles.open(file_path, "wb") as file_save:
            await file_save.write(contents)

        portfolio.main = file_name
        session.commit()

        if portfolio.main:
            file_path = os.path.join(PATH_IMAGE, old_name)
            if os.path.exists(file_path):
                os.remove(file_path)

        return PortfolioResponse(
            id=portfolio.id,
            title=portfolio.title,
            description=portfolio.description,
            main=portfolio.main,
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


@router.get(
    "/admin_portfolio_facade/{portfolio_id}/photos", response_model=list[PhotoResponse]
)
async def read_photos_facade(
    request: Request,
    portfolio_id: int,
    credentials: HTTPBasicCredentials = Depends(authenticate),
):
    try:
        photos = (
            session.query(PhotoFacade)
            .filter(PhotoFacade.portfolio_id == portfolio_id)
            .all()
        )  # Получаем фотографии по ID портфолио
        for i in photos:
            print(i.id)
        return [
            {"filename": photo.filename} for photo in photos
        ]  # Возвращаем список фотографий (может быть пустым)
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


@router.post("/admin_create_portfolio_facade", response_model=PortfolioResponse)
async def create_portfolio_facade(
    request: Request,
    title: str = Form(...),
    description: str = Form(...),
    main: UploadFile = File(...),
    credentials: HTTPBasicCredentials = Depends(authenticate),
):
    try:
        filename = f"{datetime.now()}_{main.filename}"
        portfolio = PortfolioFacade(title=title, description=description, main=filename)

        # Сохраните файл на сервере
        os.makedirs(PATH_IMAGE, exist_ok=True)
        contents = await main.read()
        file_path = os.path.join(PATH_IMAGE, filename)
        async with aiofiles.open(file_path, "wb") as file_save:
            await file_save.write(contents)

        session.add(portfolio)
        session.commit()

        return PortfolioResponse(
            id=portfolio.id,
            title=portfolio.title,
            description=portfolio.description,
            main=portfolio.main,
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


@router.post("/admin_portfolio_facade/{portfolio_id}/photos")
async def add_photos_facade(
    request: Request,
    portfolio_id: int,
    photos: List[UploadFile] = File(...),
    credentials: HTTPBasicCredentials = Depends(authenticate),
):
    try:
        saved_photos = []
        os.makedirs(PATH_IMAGE, exist_ok=True)
        for photo in photos:
            contents = await photo.read()
            file_name = f"{datetime.now()}_{photo.filename}"
            file_path = os.path.join(PATH_IMAGE, file_name)

            async with aiofiles.open(file_path, "wb") as file_save:
                await file_save.write(contents)

            new_photo = PhotoFacade(filename=file_name, portfolio_id=portfolio_id)
            session.add(new_photo)
            saved_photos.append(new_photo.filename)

        session.commit()
        return {"filenames": saved_photos}
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


@router.delete("/admin_portfolio_facade/{portfolio_id}/photos/{photo_name}")
async def delete_photo_facade(
    request: Request,
    portfolio_id: int,
    photo_name: str,
    credentials: HTTPBasicCredentials = Depends(authenticate),
):
    try:
        photo = (
            session.query(PhotoFacade)
            .filter(
                PhotoFacade.filename == photo_name,
                PhotoFacade.portfolio_id == portfolio_id,
            )
            .first()
        )
        if not photo:
            return {"error": "Фото не найдено"}, 404
        if photo:
            file_path = os.path.join(PATH_IMAGE, photo.filename)
            if os.path.exists(file_path):
                os.remove(file_path)
        session.delete(photo)
        session.commit()
        return {"message": "Фото удалено"}
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


@router.delete("/admin_delete_portfolio_facade/{portfolio_id}")
async def delete_portfolio_facade(
    request: Request,
    portfolio_id: int,
    credentials: HTTPBasicCredentials = Depends(authenticate),
):
    try:
        portfolio = (
            session.query(PortfolioFacade)
            .filter(PortfolioFacade.id == portfolio_id)
            .first()
        )
        if not portfolio:
            raise HTTPException(status_code=404, detail="Портфолио не найдено")
        photos = (
            session.query(PhotoFacade)
            .filter(PhotoFacade.portfolio_id == portfolio_id)
            .all()
        )
        for photo in photos:
            file_path = os.path.join(PATH_IMAGE, photo.filename)
            if os.path.exists(file_path):
                os.remove(file_path)
        file_path = os.path.join(PATH_IMAGE, portfolio.main)
        if os.path.exists(file_path):
            os.remove(file_path)
        session.delete(portfolio)
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
async def read_admin_roof(
    request: Request, credentials: HTTPBasicCredentials = Depends(authenticate)
):
    try:
        informs = session.query(Information).all()
        phone = session.query(Information).filter(Information.name == "phone").first()
        email = session.query(Information).filter(Information.name == "email").first()
        phone_main = get_number(phone.data)
        telegram = (
            session.query(Information).filter(Information.name == "telegram").first()
        )
        return templates.TemplateResponse(
            "admin_portfolio_roof.html",
            {
                "request": request,
                "informs": informs,
                "phone": phone,
                "email": email,
                "phone_main": phone_main,
                "telegram": telegram,
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


@router.get("/admin_portfolio_roof/{portfolio_id}", response_model=PortfolioResponse)
async def read_portfolio_roof(
    request: Request,
    portfolio_id: int,
    credentials: HTTPBasicCredentials = Depends(authenticate),
):
    try:
        portfolio = (
            session.query(PortfolioRoof)
            .filter(PortfolioRoof.id == portfolio_id)
            .first()
        )
        if not portfolio:
            raise HTTPException(status_code=404, detail="Портфолио не найдено")
        return PortfolioResponse(
            id=portfolio.id,
            title=portfolio.title,
            description=portfolio.description,
            main=portfolio.main,
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


@router.get("/admin_portfolio_roof_gallery", response_model=list[PortfolioResponse])
async def read_portfolios_roof(
    request: Request, credentials: HTTPBasicCredentials = Depends(authenticate)
):
    try:
        portfolios = session.query(PortfolioRoof).order_by(desc(PortfolioRoof.id)).all()
        return [
            PortfolioResponse(
                id=portfolio.id,
                title=portfolio.title,
                description=portfolio.description,
                main=portfolio.main,
            )
            for portfolio in portfolios
        ]
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


@router.put("/admin_portfolio_roof/{portfolio_id}", response_model=PortfolioResponse)
async def update_portfolio_roof(
    request: Request,
    portfolio_id: int,
    title: str = Form(...),
    description: str = Form(...),
    credentials: HTTPBasicCredentials = Depends(authenticate),
):
    try:
        portfolio_to_update = (
            session.query(PortfolioRoof)
            .filter(PortfolioRoof.id == portfolio_id)
            .first()
        )
        if not portfolio_to_update:
            raise HTTPException(status_code=404, detail="Портфолио не найдено")

        portfolio_to_update.title = title
        portfolio_to_update.description = description
        session.commit()
        return PortfolioResponse(
            id=portfolio_to_update.id,
            title=portfolio_to_update.title,
            description=portfolio_to_update.description,
            main=portfolio_to_update.main,
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


@router.put(
    "/admin_portfolio_roof/{portfolio_id}/main-image", response_model=PortfolioResponse
)
async def update_main_image_roof(
    request: Request,
    portfolio_id: int,
    main: UploadFile = File(...),
    credentials: HTTPBasicCredentials = Depends(authenticate),
):
    try:
        portfolio = (
            session.query(PortfolioRoof)
            .filter(PortfolioRoof.id == portfolio_id)
            .first()
        )
        if not portfolio:
            return {"error": "Портфолио не найдено"}

        old_name = portfolio.main

        os.makedirs(PATH_IMAGE, exist_ok=True)
        contents = await main.read()
        file_name = f"{datetime.now()}_{main.filename}"
        file_path = os.path.join(PATH_IMAGE, file_name)
        async with aiofiles.open(file_path, "wb") as file_save:
            await file_save.write(contents)

        portfolio.main = file_name
        session.commit()

        if portfolio.main:
            file_path = os.path.join(PATH_IMAGE, old_name)
            if os.path.exists(file_path):
                os.remove(file_path)

        return PortfolioResponse(
            id=portfolio.id,
            title=portfolio.title,
            description=portfolio.description,
            main=portfolio.main,
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


@router.get(
    "/admin_portfolio_roof/{portfolio_id}/photos", response_model=list[PhotoResponse]
)
async def read_photos_roof(
    request: Request,
    portfolio_id: int,
    credentials: HTTPBasicCredentials = Depends(authenticate),
):
    try:
        photos = (
            session.query(PhotoRoof)
            .filter(PhotoRoof.portfolio_id == portfolio_id)
            .all()
        )  # Получаем фотографии по ID портфолио
        return [
            {"filename": photo.filename} for photo in photos
        ]  # Возвращаем список фотографий (может быть пустым)
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


@router.post("/admin_create_portfolio_roof", response_model=PortfolioResponse)
async def create_portfolio_roof(
    request: Request,
    title: str = Form(...),
    description: str = Form(...),
    main: UploadFile = File(...),
    credentials: HTTPBasicCredentials = Depends(authenticate),
):
    try:
        filename = f"{datetime.now()}_{main.filename}"
        portfolio = PortfolioRoof(title=title, description=description, main=filename)

        # Сохраните файл на сервере
        os.makedirs(PATH_IMAGE, exist_ok=True)
        contents = await main.read()
        file_path = os.path.join(PATH_IMAGE, filename)
        async with aiofiles.open(file_path, "wb") as file_save:
            await file_save.write(contents)

        session.add(portfolio)
        session.commit()
        print(portfolio.id, portfolio.main)

        return PortfolioResponse(
            id=portfolio.id,
            title=portfolio.title,
            description=portfolio.description,
            main=portfolio.main,
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


@router.post("/admin_portfolio_roof/{portfolio_id}/photos")
async def add_photos_roof(
    request: Request,
    portfolio_id: int,
    photos: List[UploadFile] = File(...),
    credentials: HTTPBasicCredentials = Depends(authenticate),
):
    try:
        saved_photos = []
        os.makedirs(PATH_IMAGE, exist_ok=True)
        for photo in photos:
            contents = await photo.read()
            file_name = f"{datetime.now()}_{photo.filename}"
            file_path = os.path.join(PATH_IMAGE, file_name)

            async with aiofiles.open(file_path, "wb") as file_save:
                await file_save.write(contents)

            new_photo = PhotoRoof(filename=file_name, portfolio_id=portfolio_id)
            session.add(new_photo)
            saved_photos.append(new_photo.filename)

        session.commit()
        return {"filenames": saved_photos}
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


@router.delete("/admin_portfolio_roof/{portfolio_id}/photos/{photo_name}")
async def delete_photo_roof(
    request: Request,
    portfolio_id: int,
    photo_name: str,
    credentials: HTTPBasicCredentials = Depends(authenticate),
):
    try:
        photo = (
            session.query(PhotoRoof)
            .filter(
                PhotoRoof.filename == photo_name, PhotoRoof.portfolio_id == portfolio_id
            )
            .first()
        )
        if not photo:
            return {"error": "Фото не найдено"}, 404
        if photo:
            file_path = os.path.join(PATH_IMAGE, photo.filename)
            if os.path.exists(file_path):
                os.remove(file_path)
        session.delete(photo)
        session.commit()
        return {"message": "Фото удалено"}
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


@router.delete("/admin_delete_portfolio_roof/{portfolio_id}")
async def delete_portfolio_roof(
    request: Request,
    portfolio_id: int,
    credentials: HTTPBasicCredentials = Depends(authenticate),
):
    try:
        portfolio = (
            session.query(PortfolioRoof)
            .filter(PortfolioRoof.id == portfolio_id)
            .first()
        )
        if not portfolio:
            raise HTTPException(status_code=404, detail="Портфолио не найдено")
        photos = (
            session.query(PhotoRoof)
            .filter(PhotoRoof.portfolio_id == portfolio_id)
            .all()
        )
        for photo in photos:
            file_path = os.path.join(PATH_IMAGE, photo.filename)
            if os.path.exists(file_path):
                os.remove(file_path)
        file_path = os.path.join(PATH_IMAGE, portfolio.main)
        if os.path.exists(file_path):
            os.remove(file_path)
        session.delete(portfolio)
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
