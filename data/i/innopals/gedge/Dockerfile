FROM node:10.14.0-alpine
MAINTAINER Yuanhai He <i@bestmike007.com>
RUN apk add --no-cache tzdata && \
    rm -f /etc/localtime && cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && \
    echo "Asia/Shanghai" > /etc/timezone && date

COPY . /srv/app
WORKDIR /srv/app
RUN npm set progress=false && npm ci && npm t && npm run build

ENTRYPOINT ["node", "index.js"]
