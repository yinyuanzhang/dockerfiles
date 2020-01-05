FROM ubuntu:18.04
MAINTAINER piesecurity <admin@pie-secure.org>

RUN apt-get -qq update && \
apt-get -qq update && \
apt-get install -yq  wget curl libpcre3-dev uuid-dev libmagic-dev pkg-config g++ flex bison zlib1g-dev libffi-dev gettext libgeoip-dev make libjson-perl libbz2-dev libwww-perl libpng-dev xz-utils libffi-dev python libssl-dev libyaml-dev ethtool && \
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
# Declare args
ARG MOLOCH_VERSION=1.6.1-1_amd64
ARG UBUNTU_VERSION=18.04
ARG ES_HOST=elasticsearch
ARG ES_PORT=9200
ARG MOLOCH_PASSWORD=PASSWORDCHANGEME
ARG MOLOCH_INTERFACE=eth0
ARG CAPTURE=off
ARG VIEWER=on
#Initalize is used to reset the environment from scratch and rebuild a new ES Stack
ARG INITALIZEDB=false
#Wipe is the same as initalize except it keeps users intact
ARG WIPEDB=false

# Declare envs vars for each arg
ENV ES_HOST $ES_HOST
ENV ES_PORT $ES_PORT
ENV MOLOCH_LOCALELASTICSEARCH no
ENV MOLOCH_ELASTICSEARCH "http://"$ES_HOST":"$ES_PORT
ENV MOLOCH_INTERFACE $MOLOCH_INTERFACE
ENV MOLOCH_PASSWORD $MOLOCH_PASSWORD
ENV MOLOCHDIR "/data/moloch"
ENV CAPTURE $CAPTURE
ENV VIEWER $VIEWER
ENV INITALIZEDB $INITALIZEDB
ENV WIPEDB=$WIPEDB

RUN mkdir -p /data
RUN cd /data && curl -C - -O "https://files.molo.ch/builds/ubuntu-"$UBUNTU_VERSION"/moloch_"$MOLOCH_VERSION".deb"
RUN cd /data && dpkg -i "moloch_"$MOLOCH_VERSION".deb"

# add scripts
ADD /scripts /data/
ADD /etc /data/moloch/etc/
RUN chmod 755 /data/startmoloch.sh
RUN chmod 755 /data/wipemoloch.sh
RUN chmod 755 /data/moloch-parse-pcap-folder.sh
#Update Path
ENV PATH="/data:/data/moloch/bin:${PATH}"

EXPOSE 8005
WORKDIR /data/moloch

ENTRYPOINT ["/data/startmoloch.sh"]
  


