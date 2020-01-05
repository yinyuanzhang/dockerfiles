FROM node:8-alpine
MAINTAINER reruin

ADD . /sharelist/
WORKDIR /sharelist
VOLUME /sharelist/cache

RUN npm install

ENV HOST 0.0.0.0
ENV PORT 443

EXPOSE 443

CMD ["npm", "start"]
