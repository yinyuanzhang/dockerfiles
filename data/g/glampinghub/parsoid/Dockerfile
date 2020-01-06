FROM node:11-alpine

LABEL \
    version="1" \
    maintainer="José Luis Salvador Rufo <salvador.joseluis@gmail.com>"

ENV \
    PARSOID_VERSION=v0.10.0 \
    PARSOID_HOME=/var/lib/parsoid

RUN \
    apk add --no-cache git python make g++ \
    && mkdir -p ${PARSOID_HOME} \
    && git clone \
        --branch ${PARSOID_VERSION} \
        --single-branch \
        --depth 1 \
        --quiet \
        https://gerrit.wikimedia.org/r/p/mediawiki/services/parsoid \
        ${PARSOID_HOME} \
    && cd ${PARSOID_HOME} \
    && npm install \
    && apk del --no-cache git python make g++

EXPOSE 8000

USER node
WORKDIR ${PARSOID_HOME}
CMD ["npm", "start"]
