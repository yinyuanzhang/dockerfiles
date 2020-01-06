FROM alpine

RUN apk add --no-cache dhcp tftp-hpa
RUN touch /var/lib/dhcp/dhcpd.leases

ADD tftproot /tftproot
RUN chmod 755 /tftproot
RUN chmod 644 /tftproot/*

ADD dhcpd.conf /etc/dhcp/dhcpd.conf
RUN chmod 644 /etc/dhcp/dhcpd.conf

ADD entrypoint.sh /entrypoint.sh
RUN chmod 755 /entrypoint.sh

CMD [ "/entrypoint.sh" ]
