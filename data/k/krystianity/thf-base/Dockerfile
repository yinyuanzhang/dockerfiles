FROM phusion/baseimage:0.9.13
MAINTAINER THF "froehlingsdorf@teamhellfall.com"

ENV HOME /root
RUN /etc/my_init.d/00_regen_ssh_host_keys.sh
CMD ["/sbin/my_init"]

RUN apt-get update && \
	apt-get upgrade -y && \
	apt-get install -y sudo
	
RUN sudo apt-get install -y nano wget curl git

RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*