FROM centos/systemd

MAINTAINER boolivar <boolivar@gmail.com>

RUN true \
 && yum -y install openssh-server \
 && yum clean all

RUN true \
 && sed -i 's/#?PermitRootLogin.*/PermitRootLogin yes/' /etc/ssh/sshd_config \
 && systemctl enable sshd.service

ARG ROOT_PASSWORD=root
RUN echo root:$ROOT_PASSWORD | chpasswd

EXPOSE 22

CMD ["/usr/sbin/init"]