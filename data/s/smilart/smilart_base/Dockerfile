FROM ubuntu:14.04
MAINTAINER Smilart <support@smilart.com>

# Let's start with some basic stuff.
RUN apt-get update -qq
RUN apt-get install -qqy mc wget

# #utf-8 for "mc" and "dialog"
RUN locale-gen en_US.UTF-8
RUN echo 'export LC_ALL=en_US.utf8' >> /root/.bashrc
RUN echo 'export NCURSES_NO_UTF8_ACS=1' >> /root/.bashrc

ONBUILD ADD meta/ /meta/
ONBUILD RUN /bin/cat /meta/DESCRIPTION
ONBUILD RUN date > /meta/BUILDSTAMP
