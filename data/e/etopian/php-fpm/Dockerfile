FROM ubuntu:14.04
MAINTAINER Etopian Inc. <contact@etopian.com>

# RUN  echo 'Acquire::http { Proxy "http://172.17.42.1:3142"; };' >> /etc/apt/apt.conf.d/01proxy

ENV HOME /root
ADD . /build

RUN /build/prepare.sh && \
	/build/system_services.sh && \
	/build/utilities.sh && \
	/build/cleanup.sh

# RUN rm -f /etc/service/sshd/down

#add custom key.
# ADD id_rsa.pub /tmp/your_key.pub
# RUN cat /tmp/your_key.pub >> /root/.ssh/authorized_keys && rm -f /tmp/your_key.pub

# RUN sudo sed -i 's;www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin;www-data:x:33:33:www-data:/var/www:/bin/bash;' /etc/passwd

LABEL devoply.type=site

# EXPOSE 80 9000
EXPOSE 9000

CMD ["/sbin/my_init"]
