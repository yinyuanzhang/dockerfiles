FROM progrium/busybox

RUN opkg-install dnsmasq

EXPOSE 53

CMD ["dnsmasq", "-d"]