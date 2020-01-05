FROM rackhd/isc-dhcp-server
MAINTAINER jasl8r@alum.wpi.edu

ENV DOCKERIZE_VERSION=0.3.0

WORKDIR /dhcp

RUN apk --no-cache add openssl \
 && wget http://github.com/jwilder/dockerize/releases/download/v${DOCKERIZE_VERSION}/dockerize-alpine-linux-amd64-v${DOCKERIZE_VERSION}.tar.gz \
 && tar -C /usr/local/bin -xzvf dockerize-alpine-linux-amd64-v${DOCKERIZE_VERSION}.tar.gz \
 && rm dockerize-alpine-linux-amd64-v${DOCKERIZE_VERSION}.tar.gz

COPY dhcpd.conf.tmpl isc-dhcp-server.tmpl /dhcp/

CMD ["dockerize", \
     "-template", "/dhcp/dhcpd.conf.tmpl:/etc/dhcp/dhcpd.conf", \
     "-template", "/dhcp/isc-dhcp-server.tmpl:/etc/defaults/isc-dhcp-server", \
     "/docker-entrypoint.sh"]
