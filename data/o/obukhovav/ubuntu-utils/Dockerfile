FROM       ubuntu:16.04
MAINTAINER ObukhovAV "https://github.com/ObukhovAV"

RUN apt-get update
#RUN apt upgrade -y

#RUN apt-get install -y openssh-server
RUN apt-get install -y mc
RUN apt-get install -y nano
RUN apt-get install -y iputils-ping
RUN apt-get install -y curl
RUN apt-get install -y net-tools
RUN apt-get install -y telnet
RUN apt-get install -y dnsutils 

#RUN mkdir /var/run/sshd

#RUN echo 'root:707' |chpasswd

#RUN sed -ri 's/^#?PermitRootLogin\s+.*/PermitRootLogin yes/' /etc/ssh/sshd_config
#RUN sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config

#RUN mkdir /root/.ssh

RUN apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

#EXPOSE 22
#EXPOSE 22 443 80

#CMD    ["/usr/sbin/sshd", "-D"]
