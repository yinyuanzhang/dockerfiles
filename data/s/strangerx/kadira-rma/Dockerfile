FROM alpine:3.8

RUN echo 'http://dl-cdn.alpinelinux.org/alpine/v3.7/main' >> /etc/apk/repositories \
    && echo 'http://dl-cdn.alpinelinux.org/alpine/v3.7/community' >> /etc/apk/repositories

RUN apk add --no-cache ca-certificates nodejs npm mongodb=3.4.10-r0

WORKDIR /app

ADD ./package.json /app/
RUN npm install
ADD . /app

ENV MONGO_SHARD one
ENV MONGO_URL mongodb://dbserver/apm

CMD [ "npm", "run", "start" ]
