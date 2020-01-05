FROM alpine:3.6

ENV SERVER_ADDR     0.0.0.0
ENV SERVER_PORT     8388
ENV PASSWORD        pws
ENV METHOD          aes-256-cfb
ENV PROTOCOL        auth_sha1_v4
ENV PROTOCOLPARAM   32
ENV OBFS            http_post
ENV TIMEOUT         300
ENV DNS_ADDR        8.8.8.8
ENV DNS_ADDR_2      8.8.4.4

ARG BRANCH=manyuser
ARG WORK=~


RUN apk --no-cache add python \
    libsodium \
    wget


RUN mkdir -p $WORK && \
    wget -qO- --no-check-certificate https://github.com/hanjh310/shadowsocksr/archive/$BRANCH.tar.gz | tar -xzf - -C $WORK


WORKDIR $WORK/shadowsocksr-$BRANCH/shadowsocks


EXPOSE 8388
CMD python server.py -p $SERVER_PORT -k $PASSWORD -m $METHOD -O $PROTOCOL -o $OBFS -G $PROTOCOLPARAM
