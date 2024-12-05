FROM python:3.9-buster

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./requirements/develop.txt /requirements/develop.txt
COPY ./requirements/base.txt /requirements/base.txt

RUN pip install --upgrade pip
RUN pip install -r /requirements/develop.txt


COPY . /app/
WORKDIR /app/
