FROM alpine:3.9.3

MAINTAINER my-vue

WORKDIR /data

RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.aliyun.com/g' /etc/apk/repositories \
    && apk update \
    && apk add --no-cache nginx yarn \
    && mkdir /run/nginx

ADD package.json /data
ADD yarn.lock /data

RUN yarn

ADD . /data

RUN yarn run build

# copy configs
ADD ./docker/nginx-conf/host.conf /etc/nginx/conf.d/default.conf

ADD ./docker/entrypoint.sh /

RUN chmod +x /entrypoint.sh

EXPOSE 80

ENTRYPOINT ["/entrypoint.sh"]
