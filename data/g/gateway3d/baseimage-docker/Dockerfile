FROM ubuntu:16.04
MAINTAINER Phusion <info@phusion.nl>

ADD mirrors /etc/apt/mirrors
RUN cat /etc/apt/sources.list >> /etc/apt/mirrors && mv /etc/apt/mirrors /etc/apt/sources.list

ADD . /bd_build

RUN /bd_build/prepare.sh && \
	/bd_build/system_services.sh && \
	/bd_build/utilities.sh && \
	/bd_build/cleanup.sh

CMD ["/sbin/my_init"]
