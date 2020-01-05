FROM debian:wheezy
MAINTAINER Jonathon Fernyhough <jonathon.fernyhough@york.ac.uk>

ENV DEBIAN_FRONTEND noninteractive

ADD http://http.debian.net/debian/project/trace/ftp-master.debian.org /etc/trace_ftp-master.debian.org
ADD http://security.debian.org/project/trace/security-master.debian.org /etc/trace_security-master.debian.org

RUN apt-key adv --recv-keys --keyserver keys.gnupg.net DC242980 && \
    echo 'deb http://apt.sparkz.no/debian/ squeeze main' > /etc/apt/sources.list.d/hiawatha.list && \
    apt-get update && \
    apt-get -y upgrade && \
    apt-get -y install hiawatha

ADD hiawatha.conf /etc/hiawatha/hiawatha.conf
ADD run.sh /sbin/run-hiawatha.sh

VOLUME /var/log/hiawatha
VOLUME /var/www

EXPOSE 80

CMD ["/sbin/run-hiawatha.sh"]
