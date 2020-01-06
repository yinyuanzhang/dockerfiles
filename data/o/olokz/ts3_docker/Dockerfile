FROM ubuntu:12.04

MAINTAINER Olokz "https://github.com/Olokz"

ENV ROOT_PASS="@hyujG667$r"

RUN apt-get update

RUN apt-get install -y openssh-server
RUN mkdir /var/run/sshd

RUN echo root:"$ROOT_PASS" | chpasswd

RUN chage -d 0 root

RUN sed -ri 's/^PermitRootLogin\s+.*/PermitRootLogin yes/' /etc/ssh/sshd_config
RUN sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config

EXPOSE 21
EXPOSE 22
EXPOSE 25/udp
EXPOSE 10011
EXPOSE 30033
EXPOSE 41144
EXPOSE 2011-2050
CMD    ["/usr/sbin/sshd", "-D"]
