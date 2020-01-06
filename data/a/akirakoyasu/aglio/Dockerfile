FROM node:8.11
LABEL maintainer="Akira Koyasu <mail@akirakoyasu.net>"

ARG AGLIO_VERSION=2.3.0

RUN yarn global add aglio@${AGLIO_VERSION}
RUN mkdir -p /var/lib/aglio \
  && chown node:node /var/lib/aglio

USER node
WORKDIR /var/lib/aglio
