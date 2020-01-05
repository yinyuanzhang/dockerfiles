FROM python:3.7-alpine

ADD requirements.txt /root/requirements.txt

RUN apk update && apk upgrade && \
	apk add ca-certificates curl curl-dev py-curl build-base && \
	curl -sS https://bootstrap.pypa.io/get-pip.py | python && \
        pip install --upgrade pip && \
	pip install -r /root/requirements.txt && \
	rm -rf /var/cache/apk/*
