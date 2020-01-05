FROM node:12-alpine

LABEL maintainer=mpavei@sorint.it

ENV no_proxy=localhost \
    LOCAL_GEM=sass-3.4.22.gem \
    CHROME_BIN=/usr/bin/chromium-browser \
    TZ=Europe/Rome

COPY $LOCAL_GEM .

RUN apk add --no-cache git ruby tzdata chromium python2 && \
    gem install --local $LOCAL_GEM --no-ri --no-rdoc && \
    npm install -g npm grunt-cli karma-cli

EXPOSE 9222

ENTRYPOINT ["/bin/sh"]
