FROM fedora:29

RUN dnf update -y && dnf install -y curl php-cli php-xml php-json php-curl

COPY . /Worker
WORKDIR /Worker


#docker create --name carrental8_gw --env-file /etc/environment afindlator/carrental8_gw:1.0.1 locations.php
#docker run -it --rm --env-file ./environment carrental8_gw:latest
