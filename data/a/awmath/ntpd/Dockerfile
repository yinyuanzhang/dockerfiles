FROM fedora:latest

RUN dnf install -y ntp

EXPOSE 123/udp

CMD ["ntpd", "-n", "-b", "-g", "-l", "stdout"]
