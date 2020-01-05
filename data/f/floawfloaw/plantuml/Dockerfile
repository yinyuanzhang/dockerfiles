FROM debian:sid-slim
MAINTAINER Florent Chehab <florent.chehab@gmail.com>


# Recreate non-existent directories
RUN mkdir -p /usr/share/man/man1 /usr/share/man/man2 /usr/share/man/man3 /usr/share/man/man4 /usr/share/man/man5 /usr/share/man/man6 /usr/share/man/man7 /usr/share/man/man8


RUN apt-get update

# Install Java
RUN apt-get install -y --no-install-recommends \
      default-jre

# Install Plantuml
RUN apt-get install -y --no-install-recommends \
      plantuml \
      graphviz

# Install other stuffs
RUN apt-get install -y --no-install-recommends \  
      bash \
      make
