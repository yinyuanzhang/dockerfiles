FROM debian:jessie

RUN apt-get update && apt-get install -y \
    postgresql-client-common \
    postgresql-client-9.3

ENTRYPOINT ["psql"]
