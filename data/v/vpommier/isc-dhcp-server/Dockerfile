FROM alpine:latest

RUN apk add --update dhcp

EXPOSE 67/udp

ENTRYPOINT ["dhcpd"]
CMD ["-f", "-cf", "/etc/dhcp/dhcpd.conf", "-lf", "/var/lib/dhcp/dhcpd.leases", "--no-pid"]
