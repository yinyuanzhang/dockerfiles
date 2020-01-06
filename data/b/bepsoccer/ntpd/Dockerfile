FROM ubuntu:14.04

RUN apt-get update && apt-get install -y openntpd && apt-get clean && rm -rf /var/lib/apt/lists/*

COPY stuff/ntpd.conf /etc/openntpd/ntpd.conf

EXPOSE 123/udp
ENTRYPOINT [ "/usr/sbin/ntpd", "-v", "-d", "-s" ]