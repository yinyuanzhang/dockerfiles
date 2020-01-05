FROM alpine AS builder

RUN apk add --update alpine-sdk

ADD https://www.noip.com/client/linux/noip-duc-linux.tar.gz /usr/local/src/
WORKDIR /usr/local/src/
RUN tar xzf noip-duc-linux.tar.gz
WORKDIR /usr/local/src/noip-2.1.9-1/
RUN make



FROM alpine

WORKDIR /usr/local/bin/
COPY --from=builder /usr/local/src/noip-2.1.9-1/noip2 .

VOLUME ["/usr/local/etc/"]

CMD noip2; while pgrep noip > -; do noip2 -S; sleep 60; done; echo "noip2 process has died"; exit 1
