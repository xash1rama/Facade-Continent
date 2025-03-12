FROM python:3.9

WORKDIR /app/fasad

COPY requirements.txt /app/fasad/

RUN pip install --upgrade pip && python -m pip install -r requirements.txt

EXPOSE 5005

COPY . /app/fasad

WORKDIR /app

