FROM python:alpine

RUN apk add --no-cache ca-certificates
RUN pip install chkcrontab

COPY docker-entrypoint.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/docker-entrypoint.sh

WORKDIR /workdir
ENTRYPOINT ["docker-entrypoint.sh"]
