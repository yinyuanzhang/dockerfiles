# baseimage - start with Ubuntu 16.04
FROM ubuntu:14.04
MAINTAINER dmaligin <denis@docker.com>

# set language
ENV LANG de_DE.UTF-8
ENV LC_ALL de_DE.UTF-8
ENV VDR_LANG de_DE.UTF-8
ENV TZ Europe/Berlin

# generate locates
RUN locale-gen de_DE.UTF-8 en_US.UTF-8

# import gpg key && copy repo
COPY conf/yavdr-trusty.list /etc/apt/sources.list.d/
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 8103B360

# update the image to the latest state 
RUN apt-get update && \
  apt-get dist-upgrade -y

# install vdr, vdr-plugins 
RUN  apt-get install -y \
  vdr vdr-plugin-eepg \
  vdr-plugin-femon \
  vdr-plugin-streamdev-server \
  vdr-plugin-vnsiserver \
  vdr-plugin-wirbelscan \
  vdr-plugin-xvdr \
  vdr-plugin-ddci2 \
  vdr-plugin-dummydevice \
  vdr-plugin-live \
  vdr-plugin-epgsearch \
  vdr-plugin-svdrpservice \
  vdr-plugin-svdrposd \
  vdr-plugin-svdrpext

# copy vdr configs
COPY conf/vdr/* /var/lib/vdr/

# copy vdr plugin configs
COPY conf/plugins/* /etc/vdr/plugins/

# clean apt leftovers
RUN  apt-get clean && \
  rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# set permissions
RUN chown -R vdr:vdr /etc/vdr /var/lib/vdr /srv/vdr

ENV HOME /var/lib/vdr
WORKDIR /var/lib/vdr

# volume mappings
VOLUME /srv/vdr /etc/vdr /var/lib/vdr 

# copy startcmd
COPY runvdr.sh /

# expose necessary ports
EXPOSE 2004 3000 6419 8002 8008 34890

USER vdr

CMD [ "/runvdr.sh" ]
