FROM phusion/baseimage:0.9.19
RUN rm -rf /etc/service/sshd /etc/my_init.d/00_regen_ssh_host_keys.sh
ENV DEBIAN_FRONTEND noninteractive
ENV TERM screen

# Use baseimage-docker's init system.
CMD ["/sbin/my_init"]

RUN curl -sL https://deb.nodesource.com/setup_6.x | bash - \
  && apt-get update -q \
  && apt-get install -qy \
    nodejs \
    python2.7 \
    python-pip \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Install the latest available package.
# Pin setuptools to version 32 to avoid a race condition, see:
# https://github.com/pypa/setuptools/issues/951
RUN pip install -U \
  pip \
  setuptools==32 \
  cfscrape \
  flexget \
  transmissionrpc

# Add service files.
ADD init/ /etc/my_init.d/
ADD services/ /etc/service/
RUN chmod -v +x /etc/service/*/run
RUN chmod -v +x /etc/my_init.d/*.sh

EXPOSE 5050/tcp

VOLUME /config

# Add user.
RUN useradd -u 911 -U -s /bin/false abc \
 && usermod -G users abc
