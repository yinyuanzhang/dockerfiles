FROM phusion/baseimage:0.9.18
MAINTAINER Keith Bentrup <kbentrup@magento.com>

ENV LANG=en_US.UTF-8 TERM=xterm-256color

COPY setup.sh /etc/my_init.d/

# turn on log compression
RUN sed -i 's/^#compress/compress/' /etc/logrotate.conf 
