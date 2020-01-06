FROM debian:stretch
MAINTAINER OscarLS <olopez7@xtec.cat>

RUN apt update && apt upgrade -y && apt install apache2 -y

COPY index.html /var/wwww/html/
