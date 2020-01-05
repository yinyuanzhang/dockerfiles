FROM arm32v7/alpine

COPY qemu-arm-static /usr/bin

RUN apk update && apk upgrade
RUN apk --no-cache add dnsmasq

CMD ["/usr/sbin/dnsmasq", "-d"]
