FROM python:3.7-alpine

RUN apk update \
  # psycopg2 dependencies
  && apk add --virtual build-deps g++ gcc python3-dev musl-dev \
  && apk add postgresql-dev

COPY . .

RUN pip install -r requirements.txt

