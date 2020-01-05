FROM fernandoenzo/openvpn-client
MAINTAINER Fernando Enzo Guarini (fernandoenzo@gmail.com)

COPY ["static/openssl-sign-certs 1.0.1", "/usr/share/openssl-sign-certs/"]
COPY static/parameters.ini /usr/share/openssl-sign-certs/

COPY scripts/basics /tmp
RUN bash /tmp/basics

COPY static/server.conf /etc/openvpn/
COPY static/PC-01 /etc/openvpn/ccd/

EXPOSE 1194
EXPOSE 1194/udp

