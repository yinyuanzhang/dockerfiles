FROM debian:jessie-slim
MAINTAINER Diksy M. Firmansyah <diksy@unej.ac.id>
ENV DEBIAN_FRONTEND noninteractive

# update timezone
RUN ln -sf /usr/share/zoneinfo/Asia/Jakarta /etc/localtime
RUN dpkg-reconfigure tzdata
# update OS
RUN sed -i s/deb.debian.org/mirror.unej.ac.id/g /etc/apt/sources.list
RUN apt-get update
RUN apt-get dist-upgrade -y
# install apps
RUN apt-get install -y supervisor mysql-server openssh-server net-tools
RUN sed -i s/bind-address/#bind-address/g /etc/mysql/my.cnf
RUN mkdir /var/run/sshd/
# add config
ADD mysql-ssh.conf /etc/supervisor/conf.d/

VOLUME ["/var/lib/mysql/", "/root/.ssh/", "/var/log/supervisor/"]
EXPOSE 3306 22
ENTRYPOINT ["/usr/bin/supervisord", "-n"]
