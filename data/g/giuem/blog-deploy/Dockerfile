FROM mhart/alpine-node:6.10.3
MAINTAINER giuem<i@giuem.com>

COPY . /app
WORKDIR /app

VOLUME ["/app/pages"]

RUN apk add --no-cache git

CMD ["node", "app.js"]
