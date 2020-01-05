# Credit to https://docs.docker.com/examples/running_ssh_service/
FROM debian:jessie
MAINTAINER https://github.com/muccg/

RUN apt-get update && apt-get install -y openssh-server && apt-get clean
RUN mkdir /var/run/sshd
RUN echo 'root:root' | chpasswd
RUN sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/' /etc/ssh/sshd_config

# SSH login fix. Otherwise user is kicked off after login
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd

ENV NOTVISIBLE "in users profile"
RUN echo "export VISIBLE=now" >> /etc/profile

RUN mkdir /data

VOLUME ["/data"]

EXPOSE 22
CMD ["/usr/sbin/sshd", "-D"]
