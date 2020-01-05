FROM python:3.7.3-alpine3.9

MAINTAINER Yohei Maeda <yohei.maeda@ghs.tokyo>

RUN apk update --no-cache update && \
    apk add --no-cache unzip zip mariadb-client postgresql-dev gcc python3-dev musl-dev libffi-dev && \
    rm -rf /var/cache/apk/*


ARG DIR=/opt/app
WORKDIR $DIR
ADD ./requirements.txt ./

RUN pip install -r requirements.txt
