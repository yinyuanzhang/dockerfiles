FROM golang:1.12.9-alpine3.9

RUN apk update && \
    apk add bash ca-certificates git gcc g++ libc-dev && \
	apk add mysql mysql-client && \
	addgroup mysql mysql && \
	mkdir /scripts && \
	rm -rf /var/cache/apk/*

VOLUME ["/var/lib/mysql"]

COPY ./startup.sh /scripts/startup.sh
RUN chmod +x /scripts/startup.sh

EXPOSE 3306

RUN mkdir /app

ADD . /app

WORKDIR /app