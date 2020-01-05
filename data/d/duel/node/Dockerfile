# Base Alpine node image.
# https://hub.docker.com/_/node/
FROM node:10.17.0-alpine

RUN apk update
RUN apk add --no-cache logrotate ca-certificates openssl wget build-base
RUN wget -q https://s3-eu-west-1.amazonaws.com/obs.duel.me/docker-support/machine-names-5-char.list \
        -O /usr/share/machine-names

# VIPS lib not required for now.
# In future check http://sharp.pixelplumbing.com/en/stable/install/

RUN rm -rf /var/cache/apk/*

# Global modules.
RUN npm i -g pm2@~3.5.1

# Papertrail.
RUN wget -q https://github.com/papertrail/remote_syslog2/releases/download/v0.20/remote_syslog_linux_amd64.tar.gz \
        -O release
RUN tar -xvzf release
RUN mv remote_syslog/remote_syslog /usr/local/bin
RUN rm -rf release remote_syslog

CMD ['node']
