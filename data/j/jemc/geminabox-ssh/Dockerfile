FROM        lheinlen/geminabox
MAINTAINER  Joe Eli McIlvain <joe.eli.mac@gmail.com>

RUN apt-key update &&\
    apt-get update &&\
    apt-get install -y openssh-server
RUN mkdir /var/run/sshd
RUN echo 'root:password' | chpasswd

EXPOSE 22

CMD ["bash", "-c", "/usr/sbin/sshd && /usr/local/bin/rackup"]
