FROM node:8-alpine

RUN apk add --no-cache bash curl less groff jq python3 && \
      apk add --no-cache --virtual .build-deps gcc py3-pip python3-dev musl-dev && \
      pip3 install --upgrade pip && \
      pip3 install --upgrade awscli aws-sam-cli && \
      apk del .build-deps

VOLUME /project

WORKDIR /project