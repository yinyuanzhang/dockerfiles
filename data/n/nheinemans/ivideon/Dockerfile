############################################################
# Dockerfile to run Ivideon server
# Based on Ubuntu 12.04 LTS
############################################################
FROM ubuntu:12.04
MAINTAINER Nick Heinemans (nick@hostlogic.nl)
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update \
&& apt-get -y install wget apt-utils psmisc \
&& wget http://packages.ivideon.com/public/keys/ivideon.list -O /etc/apt/sources.list.d/ivideon.list \
&& wget -O - http://packages.ivideon.com/public/keys/ivideon.key | apt-key add - \
&& apt-get update \
&& apt-get install -y ivideon-server \
&& apt-get clean
ENTRYPOINT ["/opt/ivideon/videoserverd/videoserverd"]
