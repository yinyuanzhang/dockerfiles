FROM ubuntu:18.04

RUN apt-get update \
  && apt-get install -y haproxy rsyslog certbot openssh-server vim \
  && rm -rf /var/lib/apt/lists/*

RUN mkdir /run/haproxy

COPY ./proxy/haproxy.cfg /etc/haproxy/haproxy.cfg
COPY ./proxy/sshd_config /etc/ssh/sshd_config
COPY ./proxy/hosts.allow /etc/hosts.allow

COPY ./proxy/start ./
COPY ./proxy/renew.sh ./

RUN chmod +x ./start 
RUN chmod +x ./renew.sh 

EXPOSE 22

ENTRYPOINT [ "/start" ]