FROM ubuntu:14.04

RUN apt-get update && apt-get install -y haproxy && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /etc/haproxy

EXPOSE 80
EXPOSE 443

CMD ["haproxy", "-f", "/etc/haproxy/haproxy.cfg"]
