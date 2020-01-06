FROM coredns/coredns:latest

WORKDIR /etc/coredns
VOLUME [ "/etc/coredns" ]

EXPOSE 53/udp

ENTRYPOINT ["/coredns", "-conf", "/etc/coredns/Corefile"]