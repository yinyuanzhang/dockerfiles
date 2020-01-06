FROM alpine:latest

LABEL author="Jat <chat@jat.email>"
LABEL version="0.0.2"

RUN apk add --no-cache curl

RUN mkdir /tmp/dtunnel
WORKDIR /tmp/dtunnel

RUN curl -Lo dtunnel_linux_x64.tgz http://dog-tunnel.tk/download/linux64
RUN tar -xzf dtunnel_linux_x64.tgz

RUN install dtunnel /usr/local/bin
RUN install dtunnel_s /usr/local/bin

EXPOSE 5050 5060

ENTRYPOINT ["/usr/local/bin/dtunnel_s"]
CMD ["-addr=0.0.0.0:5050", "-addrudp=0.0.0.0:5060"]
