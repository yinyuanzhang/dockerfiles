FROM ubuntu:14.04.1

MAINTAINER Nguoi An Phu <nguoianphu@gmail.com>

ADD assets /assets
RUN /assets/setup.sh

EXPOSE 22
EXPOSE 1521
EXPOSE 8080

CMD /usr/sbin/startup.sh && /usr/sbin/sshd -D
