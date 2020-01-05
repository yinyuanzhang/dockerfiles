FROM alpine

LABEL maintainer "onisuly <onisuly@gmail.com>"

# For build image faster in China
# RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.ustc.edu.cn/g' /etc/apk/repositories

RUN apk add --no-cache --virtual .install-deps curl \
    && FRP_VERSION=$(curl -sX GET "https://api.github.com/repos/fatedier/frp/releases/latest" | awk '/tag_name/{print $5;exit}' FS='["v"]') \
    && curl -o frp.tar.gz -L https://github.com/fatedier/frp/releases/download/v${FRP_VERSION}/frp_${FRP_VERSION}_linux_amd64.tar.gz \
    && mkdir /frp \
    && tar -zxf /frp.tar.gz -C /frp --strip-components=1 \
    && rm /frp.tar.gz \
    && mkdir /conf \
    && cp /frp/frps.ini /conf/frps.ini \
    && apk del .install-deps

VOLUME ["/conf"]

EXPOSE 7000

CMD /frp/frps -c /conf/frps.ini

