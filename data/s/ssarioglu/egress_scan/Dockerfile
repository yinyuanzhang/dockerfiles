#A simple dockerfile for egress scan
FROM alpine:latest
MAINTAINER Serdar.Sarioglu@mysystem.org

RUN apk update && apk add \
	bash \
	nmap \
	nmap-scripts \
    nmap-doc \
    nmap-nping \
    nmap-ncat \
	zmap \
	busybox \
	&& rm -rf /var/cache/apk/*

CMD ["bash", "-c", "nmap -v -sS -n -p 1-65535 portquiz.net --open"]
