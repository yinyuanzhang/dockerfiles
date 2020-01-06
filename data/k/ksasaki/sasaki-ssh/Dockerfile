# sshd
#
# VERSION               0.0.1

FROM     debian
MAINTAINER Kota.S "k-sasaki@sakura.ad.jp"

# make sure the package repository is up to date
RUN apt-get update

RUN apt-get install -y openssh-server
RUN mkdir /var/run/sshd
RUN echo 'root:12345' |chpasswd

EXPOSE 22
CMD    ["/usr/sbin/sshd", "-D"]
