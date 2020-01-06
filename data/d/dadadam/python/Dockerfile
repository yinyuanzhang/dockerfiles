FROM ubuntu:18.04

MAINTAINER f1shka

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN apt-get update -y\
    && apt-get install -y locales \
    && localedef -i ru_RU -c -f UTF-8 -A /usr/share/locale/locale.alias ru_RU.UTF-8 \
    && apt-get install -y build-essential python3-dev python3-pip \
    python3-setuptools python3-wheel python3-cffi libcairo2 \
    libpango-1.0-0 libpangocairo-1.0-0 libgdk-pixbuf2.0-0 \
    libffi-dev shared-mime-info \
    && apt-get autoremove -y \
    && apt-get clean \
    && pip3 install --upgrade pip setuptools

ENV LANG ru_RU.utf8
