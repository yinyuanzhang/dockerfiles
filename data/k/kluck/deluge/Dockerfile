FROM phusion/baseimage:latest
ENV DEBIAN_FRONTEND noninteractive

# Use baseimage-docker's init system
CMD ["/sbin/my_init"]

ADD sources.list /etc/apt/
RUN apt-get update -qq
RUN apt-get install -qy deluged deluge-web unrar unzip p7zip
#Path to a directory that only contains the deluge.conf
VOLUME /config
VOLUME /downloads

EXPOSE 8112
EXPOSE 58846

# Add deluged to runit
RUN mkdir /etc/service/deluged
ADD deluged.sh /etc/service/deluged/run
RUN chmod +x /etc/service/deluged/run

# Add deluge-web to runit
RUN mkdir /etc/service/deluge-web
ADD deluge-web.sh /etc/service/deluge-web/run
RUN chmod +x /etc/service/deluge-web/run
