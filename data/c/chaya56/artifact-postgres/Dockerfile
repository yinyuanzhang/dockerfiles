FROM postgres:9.6
MAINTAINER chaya

RUN apt-get update && apt-get install -y curl
COPY run.sh /docker-entrypoint-initdb.d
RUN chmod +x /docker-entrypoint-initdb.d/run.sh