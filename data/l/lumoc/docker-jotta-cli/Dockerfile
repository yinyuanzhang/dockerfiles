FROM phusion/baseimage
MAINTAINER Lumoc

# Set correct environment variables
ENV HOME /root
ENV DEBIAN_FRONTEND noninteractive
ENV LC_ALL C.UTF-8
ENV LANG de_DE.UTF-8
ENV LANGUAGE de_DE.UTF-8


# Use baseimage-docker's init system
CMD ["/sbin/my_init"]

# Configure user nobody to match unRAID's settings
 RUN \
 usermod -u 99 nobody && \
 usermod -g 100 nobody && \
 usermod -d /home nobody && \
 chown -R nobody:users /home

# Disable SSH
RUN rm -rf /etc/service/sshd /etc/my_init.d/00_regen_ssh_host_keys.sh

RUN apt-get update && \
	apt-get -y install wget apt-transport-https ca-certificates && \
	wget -O - https://repo.jotta.us/public.gpg | apt-key add - && \
	echo "deb https://repo.jotta.us/debian debian main" | tee /etc/apt/sources.list.d/jotta-cli.list && \
	apt-get update && \
	apt-get -y install jotta-cli && \
	apt-get -y install htop

COPY root/etc/my_init.d/jottacli.sh /etc/my_init.d/11_jottacli.init
RUN chmod +x /etc/my_init.d/11_jottacli.init

VOLUME /sync
VOLUME /var/lib/jottad
