FROM alpine
RUN apk update
RUN apk add dhcp
ADD dhcpd.conf /etc/dhcpd.conf
RUN touch /var/lib/dhcp/dhcpd.leases
VOLUME /etc/
