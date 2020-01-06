FROM ubuntu:16.04

RUN apt update && apt install -y wget && wget -O - https://swupdate.openvpn.net/repos/repo-public.gpg|apt-key add - && \
	echo "deb http://build.openvpn.net/debian/openvpn/release/2.4 xenial main" > /etc/apt/sources.list.d/openvpn-aptrepo.list

RUN apt update && apt install -y openvpn easy-rsa

COPY ca.crt ca.key mc.crt mc.key ta.key dh2048.pem server.conf /etc/openvpn/

RUN echo net.ipv4.ip_forward = 1 >> /etc/sysctl.conf

EXPOSE 443/tcp

WORKDIR /etc/openvpn
#CMD etc/init.d/openvpn start

CMD openvpn --config /etc/openvpn/server.conf