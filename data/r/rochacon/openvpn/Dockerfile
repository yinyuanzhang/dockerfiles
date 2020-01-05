FROM alpine:3.8

RUN apk add --no-cache bash easy-rsa iptables openssl openvpn
RUN mkdir -p /dev/net && mknod /dev/net/tun c 10 200 

