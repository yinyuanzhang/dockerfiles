FROM node:alpine

LABEL maintainer="hyancat.cn@gmail.com"

RUN apk add --no-cache imagemagick graphicsmagick

COPY src /docker/app/
WORKDIR /docker/app
RUN yarn config set registry https://registry.npm.taobao.org && \
    yarn --only=prod

EXPOSE 3000

CMD ["node", "app.js"]
