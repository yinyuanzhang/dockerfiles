FROM python:3.6-jessie

LABEL maintainer="tech@junte.it"

RUN apt update \
    && apt install -y build-essential \
    && pip install poetry \
    && poetry config settings.virtualenvs.create false

ADD build_docs /usr/local/bin/
