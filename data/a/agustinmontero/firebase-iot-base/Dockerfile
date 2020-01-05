ARG PY_VERSION=3.6-alpine3.8
FROM python:$PY_VERSION as firebase-iot-test-base

COPY qemu-arm-static /usr/bin

RUN apk update && apk add --no-cache --virtual .build-deps gcc musl-dev wget

RUN pip3 install \
    requests==2.11.1 \
    gcloud==0.17.0 \
    oauth2client==3.0.0 \
    requests_toolbelt==0.7.0 \
    python_jwt==2.0.1 \
    pycryptodome==3.4.3 \
    RPi.GPIO \
    gpiozero \
    gps

ARG PYREBASE_VERSION=2019.1.28
RUN pip3 install https://github.com/agustinmontero/Pyrebase/releases/download/${PYREBASE_VERSION}/Pyrebase-${PYREBASE_VERSION}.tar.gz

RUN apk del .build-deps && rm -rf /var/cache/apk/*
