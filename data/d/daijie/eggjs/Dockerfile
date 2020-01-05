FROM node:9-alpine

RUN apk --update add tzdata \
    && cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime \
    && echo "Asia/Shanghai" > /etc/timezone \
    && apk del tzdata

RUN mkdir -p /usr/src/app
RUN npm i egg-init -g
WORKDIR /usr/src/app
EXPOSE 7001
ENV PATH=/usr/src/app/node_modules/.bin:$PATH

CMD npm start