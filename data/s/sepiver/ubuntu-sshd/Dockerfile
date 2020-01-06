FROM       ubuntu:18.04
MAINTAINER Aleksandar Diklic "https://github.com/rastasheep"

RUN apt-get update && apt-get install -y --no-install-recommends apt-utils

RUN apt-get install -y iputils-ping net-tools nano libssl1.0-dev wget build-essential rsyslog zlib1g-dev

RUN mkdir /var/run/sshd

RUN echo 'root:averydifficultpassword159' |chpasswd

RUN adduser --disabled-password --gecos '' sshd

ADD install-logging.sh /
RUN chmod +x /install-logging.sh 
RUN /install-logging.sh

ADD install-longtail.sh /
RUN chmod +x /install-longtail.sh
RUN /install-longtail.sh 8.1p1

RUN mkdir /root/.ssh

RUN apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

EXPOSE 22

CMD rsyslogd && /usr/sbin/sshd -f /usr/local/etc/sshd_config && tail -f /var/log/ssh.log