FROM node:alpine

# Install python
RUN apk add --update \
    python \
    python-dev \
    py-pip \
  && rm -rf /var/cache/apk/*


# Globally node-sass from NPM
RUN npm install --unsafe-perm -g node-sass
