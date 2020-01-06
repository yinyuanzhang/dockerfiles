FROM gliderlabs/alpine

MAINTAINER Pablo Palazon <ppalazon@antara.ws>

RUN apk-install unbound bind-tools

EXPOSE 53/udp 53/tcp

ADD http://www.internic.net/domain/named.root /etc/unbound/root.hints

RUN unbound-anchor -a /etc/unbound/root.key ; true

ADD remote-control /etc/unbound/remote-control
ADD *.conf /etc/unbound/

ENTRYPOINT ["/usr/sbin/unbound"]
CMD [""]
