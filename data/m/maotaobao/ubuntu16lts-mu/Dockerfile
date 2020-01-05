FROM ubuntu:16.04
MAINTAINER Francesco Sullo, sullof@sullof.com

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && apt-get -y upgrade
RUN apt-get install -y curl wget zip unzip apt-transport-https ca-certificates cron
RUN apt-get install -y openssh-server python-setuptools && /usr/bin/easy_install supervisor
RUN apt-get autoremove && apt-get autoclean

RUN useradd -ms /bin/bash paulstaab
RUN mkdir -p /home/paulstaab/.ssh
ADD adds/authorized_keys_paulstaab /home/paulstaab/.ssh/authorized_keys
RUN chmod 600 /home/paulstaab/.ssh/*
RUN chown -R paulstaab:paulstaab /home/paulstaab

ADD adds/authorized_keys /authorized_keys
ADD adds/configure.sh /configure.sh
RUN bin/bash /configure.sh && rm /configure.sh

ADD adds/supervisord.conf /etc/supervisord.conf

EXPOSE 22

CMD ["/usr/local/bin/supervisord","-n"]
