FROM docker:latest

RUN apk add --no-cache python2 py-pip \
    && pip install docker-compose \
    && apk del py-pip

COPY install/torus-cli.sh /install/torus-cli.sh
RUN /install/torus-cli.sh

COPY scripts/t /usr/bin/t
