FROM alpine:3.6


ARG BRANCH=abcd
ARG WORKR=ssr
ARG WORKS=ss



RUN apk --no-cache add python \
    libsodium \
    wget \
    git \
    bash


RUN mkdir -p $WORKR && \
    cd $WORKR && \
    git clone -b abcd https://github.com/shadowsocksR-private/shadowsocksR.git && \
    cd shadowsocksR && \
    chmod +x shadowsocks/*.sh  && \
    wget https://raw.githubusercontent.com/aiastia/ssrobf/master/config.json -O config.json && \
    cd shadowsocks && \
    ls && \
    bash run.sh





# WORKDIR $WORKR/shadowsocksr-$BRANCH/shadowsocks


#EXPOSE $SERVER_PORT
#CMD python server.py -p $SERVER_PORT -k $PASSWORD -m $METHOD -O $PROTOCOL -o $OBFS -G $PROTOCOLPARAM
