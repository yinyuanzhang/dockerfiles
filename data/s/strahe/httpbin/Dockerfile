FROM python:alpine

MAINTAINER strahe <u@strahe.com>

EXPOSE 8000

ADD gunicorn.conf gunicorn.conf

RUN apk update && \
    apk add g++ && \
    pip install --no-cache-dir cython gevent httpbin gunicorn && \
    rm -rf /var/cache/apk/*

ENTRYPOINT ["gunicorn"]
CMD ["-c", "gunicorn.conf", "httpbin:app"]
