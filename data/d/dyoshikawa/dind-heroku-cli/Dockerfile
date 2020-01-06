FROM node:10-alpine AS node
FROM docker:dind
MAINTAINER dyoshikawa

# Basic Packages
RUN apk add -U --no-cache \
    bash \
    git

# Node.js
COPY --from=node /usr/local /usr/local
RUN apk add --no-cache python make g++
RUN rm /usr/local/bin/yarn /usr/local/bin/yarnpkg

# Heroku CLI
RUN apk add --no-cache curl
RUN curl https://cli-assets.heroku.com/install.sh | sh

# User
RUN apk add sudo shadow
RUN groupadd -g 1000 dyoshikawa
RUN useradd -u 1000 -g 1000 dyoshikawa
RUN sed -e 's/# %wheel ALL=(ALL) NOPASSWD: ALL/%wheel ALL=(ALL) NOPASSWD: ALL/g' \
    -i /etc/sudoers
RUN sed -e 's/^wheel:\(.*\)/wheel:\1,dyoshikawa/g' -i /etc/group
RUN mkdir /home/dyoshikawa && chown 1000:1000 -R /home/dyoshikawa
RUN mkdir /work && chown 1000:1000 -R /work
WORKDIR /work
USER dyoshikawa
