# nginx-devel from https://launchpad.net/~chris-lea/+archive/nginx-devel
#
# VERSION	1.0

FROM ubuntu:precise
MAINTAINER Jochem Oosterveen <jochem@nextgear.nl>

RUN echo "deb http://archive.ubuntu.com/ubuntu precise main universe" > /etc/apt/sources.list
RUN echo "deb http://ppa.launchpad.net/chris-lea/nginx-devel/ubuntu precise main\ndeb-src http://ppa.launchpad.net/chris-lea/nginx-devel/ubuntu precise main" > /etc/apt/sources.list.d/chris-lea-nginx-devel-precise.list
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys C7917B12
RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install -y nginx

ENTRYPOINT ["/usr/sbin/nginx"]
CMD ["-h"]
