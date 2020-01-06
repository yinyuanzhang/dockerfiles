FROM python:alpine3.7

ADD . /srv/app

WORKDIR /srv/app/

RUN apk add postgresql-dev musl-dev gcc libffi-dev

RUN pip3 install poetry

RUN poetry install -v

WORKDIR /srv/app/src/api

EXPOSE 80

ENTRYPOINT ["/bin/sh", "-c", "echo $(ip -4 route list match 0/0 | awk '{print $3 \" host.docker.internal\"}') >> /etc/hosts && exec poetry run gunicorn -b 0.0.0.0:80 app:api"]
