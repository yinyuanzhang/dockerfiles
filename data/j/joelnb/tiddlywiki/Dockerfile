FROM node:8-slim
LABEL maintainer="joelnbarnham@gmail.com"

RUN npm install -g tiddlywiki

RUN mkdir /tiddlywiki
VOLUME ["/tiddlywiki"]

ENTRYPOINT ["tiddlywiki", "/tiddlywiki", "--server"]
