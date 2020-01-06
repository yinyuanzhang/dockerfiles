FROM debian:buster
RUN apt-get update && apt-get install bash dnsmasq -y
COPY dnsmasq.conf /etc/dnsmasq.conf
EXPOSE 53
ENTRYPOINT dnsmasq -k
