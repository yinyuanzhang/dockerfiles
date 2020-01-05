FROM postgres:10

RUN  apt-get update \
  && apt-get install -y wget \
  && rm -rf /var/lib/apt/lists/*

RUN wget -P /docker-entrypoint-initdb.d/ https://kloudio-docker.s3-us-west-2.amazonaws.com/postgres/init.sql
