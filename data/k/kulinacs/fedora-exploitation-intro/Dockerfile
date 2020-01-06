FROM kulinacs/fedora:latest

RUN dnf update -y && dnf install -y nginx && dnf clean all
RUN systemctl enable nginx

COPY ./units/simplehttpserver.service /etc/systemd/system/simplehttpserver.service
RUN systemctl enable simplehttpserver
