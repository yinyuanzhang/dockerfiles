FROM docker:18.05.0-ce-dind

LABEL maintainer="Burak Ince <burak.ince@linux.org.tr>"

RUN apk add --no-cache python3 \
  && pip3 install --upgrade pip \
  && pip install docker-compose \
  && rm -rf /var/cache/apk/*

ENTRYPOINT ["docker-compose", "version"]
