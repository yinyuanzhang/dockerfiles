# ------------------------------------------------------
#                       Dockerfile
# ------------------------------------------------------
# image:    docker-reveal.js
# tag:      latest
# name:     darioblanco/docker-reveal.js
# repo:     https://github.com/darioblanco/docker-reveal.js
# how-to:   docker build -t darioblanco/docker-reveal.js .
# Requires: node:alpine
# authors:  dblancoit@gmail.com
# ------------------------------------------------------
FROM node:10.14-alpine
LABEL maintainer="dblancoit@gmail.com"

RUN apk update && apk add git

WORKDIR /usr/src/reveal.js

RUN git clone https://github.com/hakimel/reveal.js.git .
RUN npm install

CMD ["npm", "start"]
