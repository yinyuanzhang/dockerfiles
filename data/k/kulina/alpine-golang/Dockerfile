FROM alpine:3.2
MAINTAINER Didiet Noor <dnoor@kulina.id> (@lynxluna)

ENV TERM dumb
# Patch APK Mirror to YKode
RUN echo "https://alpine.ykode.com/alpine/v3.2/main" > /etc/apk/repositories

RUN apk update && apk add go && \
  rm -rf /var/cache/apk/* && mkdir /gopath

ENV GOROOT=/usr/lib/go \
    GOPATH=/gopath \
    GOBIN=/gopath/bin
    
ENV PATH=$PATH:$GOROOT/bin:$GOPATH/bin

