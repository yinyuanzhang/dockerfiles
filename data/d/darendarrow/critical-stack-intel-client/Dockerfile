# Use phusion/baseimage as base image. To make your builds
# reproducible, make sure you lock down to a specific version, not
# to `latest`! See
# https://github.com/phusion/baseimage-docker/blob/master/Changelog.md
# for a list of version numbers.
FROM phusion/baseimage:0.11
RUN apt-get update && apt-get upgrade -y -o Dpkg::Options::="--force-confold"

# Use baseimage-docker's init system.
CMD ["/sbin/my_init"]

RUN curl https://intel.criticalstack.com/client/critical-stack-intel-amd64.deb -o /tmp/critical-stack-intel-amd64.deb
RUN dpkg -i /tmp/critical-stack-intel-amd64.deb

# Clean up APT when done.
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
