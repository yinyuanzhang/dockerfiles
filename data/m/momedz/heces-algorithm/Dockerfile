FROM python:3.7.3-slim

ENV PYTHONUNBUFFERED 1

RUN mkdir -p /app/heces

WORKDIR /app/heces

RUN pip install --upgrade pip

ADD requirements.txt /app/heces/

RUN pip install -r requirements.txt

ADD . /app/heces/
