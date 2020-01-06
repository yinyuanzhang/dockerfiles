# FROM mhart/alpine-node:8
FROM subhojit777/nightwatch:latest

LABEL maintainer="faneldabija2008@gmail.com"
USER root
RUN apk --no-cache add \
    curl \
  && npm install -g \
    pm2 \
  # Clean up obsolete files:
  && rm -rf \
    /tmp/* \
    /root/.npm

USER node