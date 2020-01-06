FROM debian:stretch
RUN echo "#!/bin/bash" > /etc/rc.local \
&&  echo "exit 0" >> /etc/rc.local \
&&  chmod +x /etc/rc.local
RUN apt-get -y update \
&&  apt-get -y install binutils \
                       dnsutils \
                       net-tools \
                       psmisc \
                       telnet \
                       tcpdump \
                       vim
