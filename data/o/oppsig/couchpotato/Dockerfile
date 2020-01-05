FROM phusion/baseimage:latest
MAINTAINER needo <needo@superhero.org>
ENV DEBIAN_FRONTEND noninteractive

# Set correct environment variables
ENV HOME /root

# Use baseimage-docker's init system
CMD ["/sbin/my_init"]

# Add a new user: kodi 
RUN useradd -u 1002 kodi 

RUN add-apt-repository "deb http://us.archive.ubuntu.com/ubuntu/ trusty universe multiverse"
RUN add-apt-repository "deb http://us.archive.ubuntu.com/ubuntu/ trusty-updates universe multiverse"
RUN apt-get update -q

# Install Dependencies
RUN apt-get install -qy python wget unrar

# Install CouchPotato v2.5.1
RUN mkdir /opt/couchpotato
RUN chown kodi:kodi /opt/couchpotato
RUN wget -P /tmp/ https://github.com/RuudBurger/CouchPotatoServer/archive/build/2.5.1.tar.gz
RUN tar -C /opt/couchpotato -xvf /tmp/2.5.1.tar.gz --strip-components 1

EXPOSE 5050

# Couchpotato Configuration
VOLUME /config
VOLUME /files

# Add edge.sh to execute during container startup
RUN mkdir -p /etc/my_init.d
ADD edge.sh /etc/my_init.d/edge.sh
RUN chmod +x /etc/my_init.d/edge.sh

# Add CouchPotato to runit
RUN mkdir /etc/service/couchpotato
ADD couchpotato.sh /etc/service/couchpotato/run
RUN chmod +x /etc/service/couchpotato/run
