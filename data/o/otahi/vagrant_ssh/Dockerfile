FROM ubuntu:14.04

MAINTAINER otahi

RUN apt-get update
RUN apt-get install -y openssh-server curl ngrep --no-install-recommends
RUN apt-get clean

USER root

RUN mkdir -p /var/run/sshd
RUN mkdir -p /root/.ssh/
ADD ./authorized_keys /root/.ssh/authorized_keys
RUN chown root:root -R /root/.ssh/
RUN chmod 600 -R /root/.ssh/

CMD /usr/sbin/sshd -D
EXPOSE 22

