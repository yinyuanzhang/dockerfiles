FROM ubuntu:16.04

COPY ./sqlite3 /usr/local/bin/sqlite3

RUN mkdir -p /var/db
WORKDIR /var/db

CMD ["tail", "-f", "/dev/null"]