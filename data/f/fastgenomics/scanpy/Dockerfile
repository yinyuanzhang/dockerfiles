FROM python:3.6.8-slim-stretch

ENV LANG C.UTF-8

COPY ./requirements.txt /requirements/
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r /requirements/requirements.txt