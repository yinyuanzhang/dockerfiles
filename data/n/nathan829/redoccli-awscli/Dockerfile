FROM node:8-alpine

RUN apk update
RUN apk add bash openssh coreutils

RUN npm install -g redoc-cli

# https://github.com/senseyeio/docker-alpine-aws-cli/blob/master/Dockerfile
RUN apk -Uuv add groff less python py-pip
RUN pip install awscli
RUN apk --purge -v del py-pip
RUN rm /var/cache/apk/*