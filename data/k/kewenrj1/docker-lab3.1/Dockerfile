FROM ubuntu:14.04
MAINTAINER Rickie Kewene "kewenrj1@student.op.ac.nz"
RUN apt-get update
RUN apt-get -y upgrade
RUN apt-get -y install openssh-server
RUN apt-get -y install apache2
RUN apt-get -y install supervisor
RUN mkdir /var/run/sshd

ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf

RUN useradd -m -G sudo user
RUN echo 'user:P@ssw0rd' | chpasswd

EXPOSE 22 80
CMD ["/usr/sbin/supervisord"]

#successfully built
