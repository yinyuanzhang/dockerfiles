FROM python:3.6-alpine3.8

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

RUN adduser docker -D -u 1000
RUN apk add --update --no-cache \
        nginx supervisor \
        libgcc libstdc++ libx11 libxml2 libxslt glib libxrender libxext libintl \
        libcrypto1.0 libssl1.0 \
        ttf-dejavu ttf-droid ttf-freefont ttf-liberation ttf-ubuntu-font-family \
        postgresql-dev pcre gnupg1 \
        git mercurial gcc musl-dev build-base linux-headers pcre-dev \
        mailcap \
        libffi-dev libxml2-dev libxslt-dev \
    && pip install --src /usr/src --no-cache-dir uwsgi pipenv poetry

COPY --from=surnet/alpine-wkhtmltopdf:3.8-0.12.5-small /bin/wkhtmltopdf /bin/wkhtmltopdf
