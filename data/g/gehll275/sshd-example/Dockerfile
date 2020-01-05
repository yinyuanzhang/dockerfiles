FROM alpine

MAINTAINER Luke Gehl <gehll275@gmail.com>

RUN apk update
RUN apk add openssh-server

ONBUILD ADD ./sshd_config /etc/ssh/sshd_config

CMD /usr/sbin/sshd -D

USER root

EXPOSE 2222



