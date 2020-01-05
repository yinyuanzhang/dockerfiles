# Use phusion/baseimage as base image
# See https://github.com/phusion/baseimage-docker/blob/master/Changelog.md for
# a list of version numbers.
FROM phusion/baseimage:0.11
LABEL maintainer="fordbaxter" 
LABEL description="Syncs an unRAID server to another. Work in progress."

VOLUME ["/config"]
VOLUME ["/home/source"]

# Use baseimage-docker's init system.
CMD ["/sbin/my_init"]

# ...put your own build instructions here...


# Clean up APT when done.
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
