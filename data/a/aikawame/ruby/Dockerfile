FROM ruby:2.5-alpine3.7

RUN echo -e "install: --no-document\nupdate: --no-document" > /etc/gemrc \
    && apk add --update --no-cache \
        bash \
        less \
        mysql-dev \
    && rm -rf /usr/mysql-test \
    && rm -f /usr/lib/libmysqld* \
    && rm -f /usr/bin/mysql*
