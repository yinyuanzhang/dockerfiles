FROM alpine:3.8
MAINTAINER Moicen Li (i@moicen.com)

# packages
RUN apk add --no-cache bash curl git gcc g++ linux-headers make nginx nodejs npm postgresql postgresql-dev readline-dev zlib zlib-dev sqlite-dev

# copy scripts
COPY setup-ruby /tmp/

RUN adduser -D admin

RUN mkdir -p /run/postgresql/
RUN chown postgres:postgres /run/postgresql/

USER postgres
RUN initdb --locale en_US.UTF-8 -E UTF8 -D '/var/lib/postgresql/data'

USER admin
WORKDIR /home/admin
RUN /tmp/setup-ruby

# switch back to `root`
USER root
