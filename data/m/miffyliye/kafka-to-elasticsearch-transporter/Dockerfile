FROM node:12
LABEL maintainer "Wang, Tao <i@miffyliye.com>"

ENV TZ Asia/Shanghai
ENV DEBUG=off \
    NODE_ENV=production

RUN mkdir -p app
WORKDIR /app
COPY . /app/

RUN yarn

CMD npm run start
