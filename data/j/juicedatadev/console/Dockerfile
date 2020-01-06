FROM python:2.7-slim-stretch
ARG DEBMIRROR=deb.debian.org

WORKDIR /usr/src/app
RUN sed -i "s/deb.debian.org/$DEBMIRROR/g" /etc/apt/sources.list && \
  sed -i "s/security.debian.org/$DEBMIRROR/g" /etc/apt/sources.list && \
  apt-get update && apt-get install --no-install-recommends -y curl fuse locales gettext build-essential busybox-syslogd && \
  echo 'en_US.UTF-8 UTF-8' > /etc/locale.gen && \
  locale-gen &&	\
  mkdir -p /root/.local && \
  curl -L -o /tmp/bats.tar.gz https://github.com/sstephenson/bats/archive/master.tar.gz && \
  tar xvf /tmp/bats.tar.gz -C /tmp/ && \
  /tmp/bats-master/install.sh /usr && \
  rm -rf /tmp/bats-master bats.tar.gz && \
  apt-get clean -y && \
  apt-get autoclean -y && \
  apt-get autoremove -y && \
  rm -rf /var/log/* /var/lib/apt/lists/* /var/cache/*

ENV LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8
