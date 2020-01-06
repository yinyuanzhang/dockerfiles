FROM ubuntu:18.04
MAINTAINER Pujianto <mailto@pujianto.net>
ENV ROOT_PASSWORD "root"
RUN apt-get update -y
RUN apt-get install openssh-server -y
RUN mkdir /var/run/sshd
RUN echo "SSHD_OPTS='-E /var/log/sshd.log'" > /etc/default/ssh 
RUN ( grep /etc/ssh/sshd_config -e PermitRootLogin && sed -r 's/(#|)PermitRootLogin(.*)/PermitRootLogin yes/' -i /etc/ssh/sshd_config ) || echo "PermitRootLogin yes" >> /etc/ssh/sshd_config
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
EXPOSE 22
CMD ["/bin/bash"]
