FROM alpine
ARG VERSION=6.2
RUN mkdir /gp && cd /gp && \
    wget https://github.com/snail007/goproxy/releases/download/v${VERSION}/proxy-linux-amd64.tar.gz && \
    tar xvzf proxy-linux-amd64.tar.gz && rm proxy-linux-amd64.tar.gz
RUN mkdir /data
WORKDIR /gp
VOLUME ["/data"]
EXPOSE 33080
CMD ./proxy ${OPTS}