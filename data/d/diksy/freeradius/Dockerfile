FROM debian:stretch
MAINTAINER Diksy M. Firmansyah <diksy@unej.ac.id>
# update timezone
RUN ln -sf /usr/share/zoneinfo/Asia/Jakarta /etc/localtime
RUN dpkg-reconfigure -f noninteractive tzdata
# update OS
RUN sed -i s/deb.debian.org/mirror.unej.ac.id/g /etc/apt/sources.list
RUN apt-get update
RUN apt-get dist-upgrade -y
# install freeradius
RUN apt-get install -y freeradius freeradius-mysql

VOLUME ["/etc/freeradius/3.0/", "/var/log/freeradius/"]
EXPOSE 1812/udp
ENTRYPOINT ["/usr/sbin/freeradius", "-f"]
