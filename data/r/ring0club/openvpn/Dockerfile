FROM alpine:3.9
RUN apk upgrade --no-cache
RUN apk add openvpn=2.4.7-r1 \
    --repository https://nl.alpinelinux.org/alpine/edge/main \
    --no-cache
#VOLUME /etc/openvpn
ENTRYPOINT ["openvpn"]
CMD ["--config", "/etc/openvpn/server.conf"]
