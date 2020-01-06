FROM alpine:3.6

RUN set -ex \
    && apk add --no-cache libsodium py2-pip \
    && pip --no-cache-dir install https://github.com/shadowsocks/shadowsocks/archive/master.zip
RUN echo 'nameserver 119.29.29.29' >> /etc/resolv.conf \
    && echo 'nameserver 223.5.5.5' >> /etc/resolv.conf
    
ADD config.json /config.json

EXPOSE 443

ENTRYPOINT ["ssserver", "-c", "/config.json"]
