FROM python:3.7.3-slim

ENV PYTHONUNBUFFERED 1

RUN mkdir -p /app/hscmstream

WORKDIR /app/hscmstream

RUN pip install --upgrade pip

ADD requirements.txt /app/hscmstream/

RUN pip install -r requirements.txt

ADD . /app/hscmstream/
