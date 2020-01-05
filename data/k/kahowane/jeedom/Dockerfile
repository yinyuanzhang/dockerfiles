ARG DEBIAN_VERSION=9.11

FROM debian:$DEBIAN_VERSION

ENV SHELL_ROOT_PASSWORD Mjeedom96
ENV APACHE_PORT 80
ENV SSH_PORT 22
ENV MODE_HOST 0

RUN apt-get update -y && \
  apt-get install -y wget openssh-server supervisor mariadb-client

RUN echo "root:${SHELL_ROOT_PASSWORD}" | chpasswd && \
  sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/' /etc/ssh/sshd_config && \
  sed -i 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' /etc/pam.d/sshd

RUN mkdir -p /var/run/sshd /var/log/supervisor

RUN rm /etc/motd
RUN wget https://raw.githubusercontent.com/jeedom/core/release/install/motd -O /etc/motd

RUN rm /root/.bashrc
RUN wget https://raw.githubusercontent.com/jeedom/core/release/install/bashrc -O /root/.bashrc

RUN wget https://raw.githubusercontent.com/jeedom/core/release/install/OS_specific/Docker/supervisord.conf -O /etc/supervisor/conf.d/supervisord.conf

RUN wget https://raw.githubusercontent.com/jeedom/core/release/install/install.sh -O /root/install_docker.sh
RUN chmod +x /root/install_docker.sh

RUN /root/install_docker.sh -s 1;exit 0
RUN /root/install_docker.sh -s 2;exit 0
RUN /root/install_docker.sh -s 4;exit 0
RUN /root/install_docker.sh -s 5;exit 0
RUN /root/install_docker.sh -s 7;exit 0
RUN /root/install_docker.sh -s 10;exit 0

RUN systemctl disable apache2;exit 0
RUN systemctl disable sshd;exit 0

RUN wget https://raw.githubusercontent.com/jeedom/core/release/install/OS_specific/Docker/init.sh -O /root/init.sh
RUN chmod +x /root/init.sh

CMD ["/root/init.sh"]
