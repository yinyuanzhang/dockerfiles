FROM debian:stretch-slim
RUN apt update && env DEBIAN_FRONTEND=noninteractive apt install -y dns2tcp

EXPOSE 53
CMD [ "dns2tcpd", "-f", "/dns2tcpd.conf", "-F", "-d", "2" ]
