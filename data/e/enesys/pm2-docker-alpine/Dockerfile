FROM node:10-alpine
MAINTAINER Enesys

RUN apk --update add gcc g++ make python tzdata bash git pdftk poppler-utils && npm install pm2 -g && npm install node-gyp -g && \
  cp /usr/share/zoneinfo/Europe/Paris /etc/localtime && \
    apk del tzdata && \
    rm -rf /var/cache/apk/*
    
EXPOSE 3300 8080

VOLUME ["/app"]

WORKDIR /app

# Start process.yml
CMD echo $NODE_ENV $PROCESS_FILE && npm install --unsafe-perm && pm2-docker start $PROCESS_FILE --env $NODE_ENV
