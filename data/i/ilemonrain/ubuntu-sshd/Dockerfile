FROM ubuntu:18.04

LABEL MAINTAINER iLemonrain "ilemonrain@ilemonrain.com"

RUN (echo "nameserver 8.8.8.8" >> /etc/resolv.conf ;\
     apt-get update ;\
     apt-get upgrade -y ;\
     apt-get install -y openssh-server language-pack-en language-pack-en-base ;\
     mkdir /var/run/sshd ;\
     echo 'root:ubuntu' |chpasswd ;\
     sed -ri 's/^PermitRootLogin\s+.*/PermitRootLogin yes/' /etc/ssh/sshd_config ;\
     sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config ;\
     apt-get clean && apt-get autoclean )

EXPOSE 22

CMD ["/usr/sbin/sshd", "-D"]