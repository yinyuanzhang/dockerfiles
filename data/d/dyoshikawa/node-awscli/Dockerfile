FROM node:6-alpine
MAINTAINER dyoshikawa

# install aglio
RUN apk add -U --no-cache --virtual .gyp make g++ python
RUN npm i -g aglio
RUN apk del .gyp

# install pip
RUN apk add --no-cache py-pip
RUN pip install --upgrade pip

# install awscli
RUN pip install awscli
