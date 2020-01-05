# A image with phantomjs 2.0.0
# For more information; https://github.com/rdpanek/docker_phantomjs

# VERSION 2.0.0

FROM rdpanek/base:1.0
MAINTAINER Radim Daniel Pánek <rdpanek@gmail.com>

# env
ENV PHANTOMJS_VERSION 2.0.0


# Commands
RUN \
  apt-get update && \
  apt-get install -y build-essential g++ flex bison gperf ruby perl \
  libsqlite3-dev libfontconfig1-dev libicu-dev libfreetype6 libssl-dev \
  libpng-dev libjpeg-dev && \
  mkdir -p /srv/var && \
  git clone https://github.com/rdpanek/phantomjs /srv/var/phantomjs && \
  cd /srv/var/phantomjs && \
  git ch -b yosemite && git pull origin yosemite && \
  git l -5 && \
  ./build.sh --confirm && \
  ln -s /srv/var/phantomjs/bin/phantomjs /usr/bin/phantomjs && \
  apt-get autoremove -y && \
  apt-get clean all

# Default command
CMD ["/usr/bin/phantomjs"]