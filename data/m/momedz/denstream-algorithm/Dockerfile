FROM python:3.7.3-slim

ENV PYTHONUNBUFFERED 1

RUN mkdir -p /app/denstream

WORKDIR /app/denstream

RUN pip install --upgrade pip

ADD requirements.txt /app/denstream/

RUN pip install -r requirements.txt

ADD . /app/denstream/
