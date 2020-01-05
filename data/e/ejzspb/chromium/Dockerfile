#
# Build Chromium image
#

FROM ubuntu:latest
MAINTAINER Ejz <ejz@ya.ru>

RUN apt-get update
ENV DEBIAN_FRONTEND noninteractive
RUN apt-get install -y \
    pulseaudio \
    python-psutil \
    supervisor \
    wget \
    x11vnc \
    xbase-clients \
    xdg-utils \
    xvfb \
    chromium-browser
RUN apt-get install -y \
    php5-cli php5-common php5-fpm php5-cgi \
    php5-mysql php5-sqlite php5-curl php5-gd php5-mcrypt
RUN apt-get install -y xdotool
RUN apt-get install -y openssh-server
RUN apt-get install -y scrot
RUN mkdir /var/run/sshd
RUN echo 'root:root' | chpasswd
RUN sed -i 's/PermitRootLogin .*/PermitRootLogin yes/' /etc/ssh/sshd_config
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd
ENV NOTVISIBLE "in users profile"
RUN echo "export VISIBLE=now" >> /etc/profile
ENV proxy=""
ENV passwd passwd
ENV url http://yahoo.com
ENV devtools http://site.com/devtools.html?ws=
ENV x11vnc 1
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf
ADD ./chromium-master.sh /usr/local/bin/chromium-master.sh
RUN chmod +x /usr/local/bin/chromium-master.sh
ADD ./chromium-slave.sh /usr/local/bin/chromium-slave.sh
RUN chmod +x /usr/local/bin/chromium-slave.sh
ADD ./x11vnc.sh /usr/local/bin/x11vnc.sh
RUN chmod +x /usr/local/bin/x11vnc.sh
ADD ./ws.php /usr/local/bin/ws.php
RUN chmod +x /usr/local/bin/ws.php
RUN mkdir -p /tmp/chromium
RUN useradd -m -G pulse-access chromium

VOLUME ["/home/chromium"]
EXPOSE 5900
EXPOSE 5901
EXPOSE 22
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]
