FROM node:8-alpine

RUN apk --no-cache add openjdk11 --repository=http://dl-cdn.alpinelinux.org/alpine/edge/community
RUN npm i -g firebase-tools && firebase setup:emulators:database

CMD ["tail", "-f", "/dev/null"]