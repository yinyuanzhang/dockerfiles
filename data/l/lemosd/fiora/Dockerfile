FROM node:alpine

WORKDIR /usr/src/app

Run wget -q -O - https://api.github.com/repos/yinxin630/fiora/tarball/master | tar xz --strip=1 && \
    apk add --no-cache python build-base && \
    yarn install && \
    yarn build && \
    rm -rf public/* && \
    mv dist/fiora/* public

CMD [ "node", "server/main.js" ]
