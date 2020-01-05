FROM node:10.7

LABEL maintainer="YING WANG <864891814@qq.com>"

WORKDIR /app
COPY . /app

RUN    rm package-lock.json \
    ; rm -rf .idea \
    ; rm -rf node_modules \
    ; npm config set registry "https://registry.npm.taobao.org/" \
    && npm install

EXPOSE 3000
CMD [ "npm", "start", "daemon off;"]
