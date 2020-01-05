FROM debian:jessie-slim
MAINTAINER Diksy M. Firmansyah <diksy@unej.ac.id>
ENV DEBIAN_FRONTEND noninteractive

# update timezone
RUN ln -sf /usr/share/zoneinfo/Asia/Jakarta /etc/localtime
RUN dpkg-reconfigure -f noninteractive tzdata
# update OS
RUN sed -i s/deb.debian.org/mirror.unej.ac.id/g /etc/apt/sources.list
RUN apt-get update
RUN apt-get dist-upgrade -y
# install openssh-server
RUN apt-get install -y openssh-server
RUN mkdir /var/run/sshd/

VOLUME /root/.ssh
EXPOSE 22
ENTRYPOINT ["/usr/sbin/sshd", "-D"]
