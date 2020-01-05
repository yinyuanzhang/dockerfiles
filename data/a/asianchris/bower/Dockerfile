FROM node:7.9.0
MAINTAINER Chris Baptista

WORKDIR /src

RUN npm install --silent -g bower@1.8.0

RUN mkdir /.config && chmod -R 777 /.config \
    && mkdir /.cache && chmod -R 777 /.cache \
    && mkdir /.local && chmod -R 777 /.local

VOLUME ["/src"]

ENTRYPOINT ["bower"]
