FROM alpine:3

RUN apk update && apk add --no-cache dhcp && touch /var/lib/dhcp/dhcpd.leases

EXPOSE 67/udp 67/tcp

ENTRYPOINT ["/usr/sbin/dhcpd"]
CMD ["-4", "-f", "-d", "--no-pid"]
