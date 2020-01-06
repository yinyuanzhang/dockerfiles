FROM alpine

ENV SERVER_ADDR 0.0.0.0
ENV SERVER_PORT 2333
ENV PASSWORD    2333
ENV METHOD      aes-128-ctr
ENV PROTOCOL    auth_aes128_md5
ENV OBFS        tls1.2_ticket_auth
ENV TIMEOUT     300
ENV LOCAL_PORT  8992


RUN apk update \
    && apk add python \
    libsodium \
    unzip \
    wget \
  && rm -rf /var/cache/apk/*


RUN wget --no-check-certificate https://github.com/breakwa11/shadowsocks/archive/manyuser.zip -O /tmp/manyuser.zip \
    && unzip -d /tmp /tmp/manyuser.zip \
    && mv /tmp/shadowsocksr-manyuser/shadowsocks ~/shadowsocks \
    && rm -rf /tmp/*


WORKDIR ~/shadowsocks


CMD python ~/shadowsocks/local.py -p $SERVER_PORT -b 0.0.0.0 -s $SERVER_ADDR -k $PASSWORD -l $LOCAL_PORT -m $METHOD -O $PROTOCOL -o $OBFS
