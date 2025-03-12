from sqlalchemy import (
    String,
    BigInteger,
    Integer,
    Column,
    DateTime,
    ForeignKey,
    desc,
    Boolean,
)
from sqlalchemy.orm import relationship
from datetime import datetime
from .database import Base, session, engine, Session


class FacadeStart(Base):
    __tablename__ = "facadestarts"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    measure = Column(String, default="м²")
    price = Column(BigInteger, nullable=False)



class FacadeBase(Base):
    __tablename__ = "facadebases"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    measure = Column(String, default="м²")
    price = Column(BigInteger, nullable=False)


class FacadeFinish(Base):
    __tablename__ = "facadefinish"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    measure = Column(String, default="м²")
    price = Column(BigInteger, nullable=False)


class RoofStart(Base):
    __tablename__ = "roofstarts"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    measure = Column(String, default="м²")
    price = Column(BigInteger, nullable=False)


class RoofBase(Base):
    __tablename__ = "roofbases"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    measure = Column(String, default="м²")
    price = Column(BigInteger, nullable=False)


class RoofFinish(Base):
    __tablename__ = "roofsfinish"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    measure = Column(String, default="м²")
    price = Column(BigInteger, nullable=False)


class Information(Base):
    __tablename__ = "informations"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    data = Column(String)


class Admin(Base):
    __tablename__ = "admins"

    id = Column(Integer, primary_key=True, index=True)
    login = Column(String, index=True)
    password = Column(String, index=True)


class Contact(Base):
    __tablename__ = "contacts"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    number_phone = Column(String, nullable=False)
    question = Column(String, nullable=False)
    comments = Column(String)
    date = Column(DateTime, default=datetime.now)


class PortfolioFacade(Base):
    __tablename__ = "portfolio_facade"

    id = Column(Integer, primary_key=True)
    title = Column(String)  # Название портфолио
    description = Column(String)  # Описание
    main = Column(String)  # Название файла главной картинки
    photos = relationship(
        "PhotoFacade", backref="portfolio_facade"
    )  # Связь с фотографиями


class PortfolioRoof(Base):
    __tablename__ = "portfolio_roof"

    id = Column(Integer, primary_key=True)
    title = Column(String)  # Название портфолио
    description = Column(String)  # Описание
    main = Column(String)  # Название файла главной картинки
    photos = relationship("PhotoRoof", backref="portfolio_roof")  # Связь с фотографиями


class PhotoFacade(Base):
    __tablename__ = "photo_facade"
    id = Column(Integer, primary_key=True)
    filename = Column(String)  # Название файлов галереи
    portfolio_id = Column(Integer, ForeignKey("portfolio_facade.id"))


class PhotoRoof(Base):
    __tablename__ = "photo_roof"
    id = Column(Integer, primary_key=True)
    filename = Column(String)  # Название файлов галереи
    portfolio_id = Column(Integer, ForeignKey("portfolio_roof.id"))
