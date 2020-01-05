FROM ubuntu:16.04
MAINTAINER kevinosorus <kevin.caradant@gmail.com>
RUN apt-get update && apt-get upgrade -y && apt-get install -y software-properties-common tzdata debconf-utils

#lirc
RUN mkdir /etc/lirc
RUN echo 'lirc lirc/remote select Windows Media Center Transceivers/Remotes (all)' > /etc/lirc/lirc_mce.seed
RUN echo 'lirc lirc/transmitter select None' >> /etc/lirc/lirc_mce.seed
RUN debconf-set-selections /etc/lirc/lirc_mce.seed
RUN apt-get install -y --force-yes -q lirc
RUN rm -f /etc/lirc/lirc_mce.seed


RUN mkdir /var/run/lirc/
RUN ln -sf /dev/lircd /var/run/lirc/lircd

RUN add-apt-repository -y ppa:team-xbmc/ppa
RUN apt-get update && apt-get install -y kodi kodi-pvr-nextpvr
RUN ln -fs /usr/share/zoneinfo/Europe/Paris /etc/localtime && dpkg-reconfigure -f noninteractive tzdata
ENTRYPOINT [ "/usr/bin/kodi", "--lircdev /dev/lircd" ]


