FROM docker:18.06
MAINTAINER Simon Bäumer

ENV GOSS_FILES_STRATEGY=cp
ENV GOSS_VERSION=v0.3.6
ENV GOSS_PATH=/usr/bin/goss
ENV CONTAINER_NAME=""

RUN mkdir /goss

RUN apk add \
    wget \
    bash

RUN wget https://github.com/aelsabbahy/goss/releases/download/${GOSS_VERSION}/goss-linux-amd64 -O /usr/bin/goss
RUN chmod +x /usr/bin/goss

RUN wget https://github.com/aelsabbahy/goss/releases/download/${GOSS_VERSION}/dgoss -O /usr/bin/dgoss
RUN chmod +x /usr/bin/dgoss

VOLUME /goss

WORKDIR /goss

CMD [ "/bin/bash", "-c",  "GOSS_FILES_STRATEGY=${GOSS_FILES_STRATEGY} GOSS_PATH=${GOSS_PATH} dgoss run ${CONTAINER_NAME}" ]
