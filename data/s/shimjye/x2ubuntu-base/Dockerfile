FROM ubuntu:16.04
LABEL maintainer="shimjye@gmail.com"

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update
RUN apt-get install -y openssh-server xubuntu-desktop pwgen

RUN mkdir -p /var/run/sshd && sed -i "s/UsePrivilegeSeparation.*/UsePrivilegeSeparation no/g" /etc/ssh/sshd_config && sed -i "s/UsePAM.*/UsePAM no/g" /etc/ssh/sshd_config
RUN sed -i "s/PermitRootLogin.*/PermitRootLogin yes/g" /etc/ssh/sshd_config
RUN sed -i "s/#PasswordAuthentication/PasswordAuthentication/g" /etc/ssh/sshd_config

RUN mkdir -p /tmp/.X11-unix && chmod 1777 /tmp/.X11-unix
RUN mkdir /var/run/dbus

ADD set_root_pw.sh /set_root_pw.sh
ADD run.sh /run.sh
RUN chmod +x /*.sh

EXPOSE 22

CMD ["/run.sh"]
