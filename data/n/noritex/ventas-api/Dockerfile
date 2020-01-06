FROM tiangolo/uvicorn-gunicorn:python3.7-alpine3.8
LABEL maintainer="Leonel Atencio<leonela@noritex.com>"

COPY requirements.txt ./

RUN apk add --no-cache --virtual .build-deps gcc g++ unixodbc-dev freetds-dev
RUN pip install --upgrade pip
RUN pip install -r ./requirements.txt

COPY ./app /app