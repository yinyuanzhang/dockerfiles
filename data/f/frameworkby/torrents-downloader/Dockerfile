FROM  python:3.6-alpine

RUN apk add --no-cache g++ linux-headers postgresql-dev libffi-dev

COPY requirements.txt /tmp/requirements.txt

RUN pip install --upgrade pip && pip install --upgrade --src=/tmp -r tmp/requirements.txt

COPY ./src /app

WORKDIR /app

RUN mkdir /app/torrents

# CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver"]
