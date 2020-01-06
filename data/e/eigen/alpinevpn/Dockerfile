FROM alpine
RUN apk --no-cache add openssl openvpn iptables curl
ADD ./bin /sbin
EXPOSE 1194/udp
CMD run
