FROM python:3.10.7-slim-buster

RUN apt-get update \
  && apt-get install -y build-essential \
  && apt-get install -y libpq-dev

WORKDIR /usr/src

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/requirements.txt
RUN pip install -r requirements.txt

COPY . /usr/src/