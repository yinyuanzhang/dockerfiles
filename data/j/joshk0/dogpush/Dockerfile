FROM python:2.7-alpine

ADD requirements.txt /

RUN apk add --no-cache --virtual .build-deps \
      gcc \
      freetype-dev \
      musl-dev && \
    pip install -r /requirements.txt && \
    apk del .build-deps

ADD . /

ENTRYPOINT ["/dogpush/dogpush.py"]
