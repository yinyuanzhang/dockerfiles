FROM python:2.7-alpine

RUN apk add --no-cache --virtual .build-deps \
    gcc musl-dev \
    libxslt-dev libxml2-dev &&\
    pip install lxml && \
    apk del .build-deps && \
    apk add --no-cache libxslt libxml2

CMD ["python2"]
