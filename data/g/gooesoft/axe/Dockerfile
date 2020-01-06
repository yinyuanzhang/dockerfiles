FROM python:3.6-alpine

RUN apk update 
RUN apk add openssl-dev
RUN apk add gcc python3-dev musl-dev libffi-dev
RUN pip install cryptography==2.0.3
RUN apk del openssl-dev

RUN set -ex \
    && apk add --no-cache --update \
    build-base \
    ttf-dejavu \ 
    gcc \
    make \
    libc-dev \
    linux-headers \
    pcre-dev \
    zlib-dev \
    libressl-dev \
    libffi \
    gdk-pixbuf \
    jpeg-dev \
    postgresql-dev \
    cairo-dev \
    pango-dev \
    libmagic \
    cairo \
    pango \
    glib \
    git \
    nginx \
    supervisor \
    nodejs \
  && rm -rf /var/cache/apk/* && \
  chown -R nginx:www-data /var/lib/nginx

RUN pip install uwsgi
RUN pip install weasyprint

COPY ./requirements.txt /requirements.txt
RUN pip install --no-cache-dir -r /requirements.txt

COPY ./fonts /usr/share/fonts
RUN fc-cache
