FROM debian:jessie
MAINTAINER Jivan Kulkarni <jivank@gmail.com>


RUN apt-get update && \
    apt-get install -y openssh-client && \
    apt-get clean

ADD start.sh /root/
RUN chmod +x /root/start.sh

CMD ["/root/start.sh"]