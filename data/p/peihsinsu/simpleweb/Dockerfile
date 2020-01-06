FROM peihsinsu/alpine-nodejs

RUN npm install express-generator -g &&\
  rm -rf /var/cache/apk/*

ENV PATH $PATH:/usr/bin
WORKDIR /app

ADD web/ /app/

ENTRYPOINT ["/usr/bin/npm", "start"]

