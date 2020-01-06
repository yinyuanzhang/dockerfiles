# Base OS
FROM centos:5
MAINTAINER info@incendonet.com

# Env setup
ENV HOME /root
WORKDIR ~/

# Build deps
RUN \
	yum -y update && \
	yum -y install glibc.i686 expat-devel.i386 libstdc++.i386 openssl-devel.i386
