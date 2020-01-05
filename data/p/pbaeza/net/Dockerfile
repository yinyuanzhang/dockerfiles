FROM ubuntu:latest

ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

RUN apt-get update \
	&& apt install -yq dnsutils telnet curl pgcli mysql-client inetutils-traceroute inetutils-ping time wget netcat ssh-client tcpdump \
	&& apt clean \
	&& rm -rf /var/lib/apt/lists
