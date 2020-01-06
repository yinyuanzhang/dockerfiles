FROM lemonlatte/docker-webvirtmgr
MAINTAINER Tamaki Nishino <otamachan@gmail.com>

RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get -y install python-numpy
RUN pip install websockify
ADD supervisor.webvirtmgr.conf /etc/supervisor/conf.d/webvirtmgr.conf

EXPOSE 6080
