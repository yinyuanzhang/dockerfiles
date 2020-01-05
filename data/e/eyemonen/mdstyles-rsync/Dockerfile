FROM node:10-alpine

LABEL maintainer="dev.eyemonen@gmail.com"

WORKDIR /home/mdgen

RUN apk add --no-cache openssh-client rsync && \
  npm install -g markdown-styles && \ 
  addgroup -S mdgen && \
  adduser -S mdgen -G mdgen
  
COPY eyemonen-coursestyle /usr/local/lib/node_modules/markdown-styles/layouts/eyemonen-coursestyle

USER mdgen
CMD ["/bin/sh"]
