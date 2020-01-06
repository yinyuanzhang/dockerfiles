from alpine:latest as builder

RUN apk --no-cache add make musl-dev git gcc
run git clone https://github.com/ryanmjacobs/darkhttpd
workdir darkhttpd
copy filetype.patch .
run patch darkhttpd.c < filetype.patch 
run LDFLAGS=-static make bin

from scratch
LABEL maintainer="containsliquid@project47.xyz"
expose 8080
#workdir /usr/local/bin
copy --from=builder /darkhttpd/darkhttpd .
workdir /data
entrypoint ["../darkhttpd", ".", "--port", "8080"]
