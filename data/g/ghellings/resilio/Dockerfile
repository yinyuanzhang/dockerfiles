FROM resilio/sync:release-2.4.4
MAINTAINER Greg Hellings <greg@thesub.net>

RUN apt-get clean && apt-get update && apt-get install -y wget

ENV \
  DOCKERIZE_VERSION=v0.3.0 \
  SECRET="" \
  SYNCPATH="/data"

RUN wget https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && tar -C /usr/local/bin -xzvf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && rm dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && mkdir -p /templates \
    && mkdir -p /resilio/.sync \
    && mkdir -p var/run/resilio \
    && mkdir -p $SYNCPATH

COPY sync.cfg.tmpl /templates/sync.cfg.tmpl

ENTRYPOINT [ \
  "dockerize", \
  "-template", "/templates/sync.cfg.tmpl:/etc/sync.cfg", \
  "/usr/bin/rslsync", \
  "--nodaemon", \
  "--config", "/etc/sync.cfg" \
]