FROM python:3.7-stretch

RUN apt-get update && apt-get install -y cron git nano jq && rm -rf /var/lib/apt/lists/*

RUN pip3 install --no-cache-dir pipenv

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

ONBUILD COPY Pipfile /usr/src/app/
ONBUILD COPY Pipfile.lock /usr/src/app/

ONBUILD RUN set -ex && pipenv install --deploy --system

ONBUILD COPY . /usr/src/app
