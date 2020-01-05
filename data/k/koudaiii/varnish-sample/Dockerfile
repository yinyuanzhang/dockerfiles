FROM        ubuntu:14.04.2
MAINTAINER  koudaiii "cs006061@gmail.com"
ENV REFRESHED_AT 2015-11-16

# Update the package repository and install applications
# https://www.varnish-cache.org/docs/4.1/installation/install.html#build-dependencies-on-debian-ubuntu
RUN apt-get update -qq && \
  apt-get upgrade -yqq && \
  apt-get -yqq install apt-transport-https && \
  apt-get -yqq install curl && \
  curl https://repo.varnish-cache.org/GPG-key.txt | apt-key add - && \
  echo "deb https://repo.varnish-cache.org/ubuntu/ trusty varnish-4.1" >> /etc/apt/sources.list.d/varnish-cache.list && \
  apt-get  update -qq && \
  apt-get -yqq install varnish && \
  apt-get -yqq clean

ADD start.sh /start.sh

# Make our custom VCLs available on the container
ADD config/default.vcl /etc/varnish/default.vcl
ADD config/varnish /etc/default/varnish

CMD ["/start.sh"]
