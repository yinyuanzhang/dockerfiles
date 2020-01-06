FROM alpine:latest

RUN apk add socat
CMD socat -d -d -u TCP:decoder:30005 TCP:feed.adsbexchange.com:${RECEIVER_PORT:-30005}
