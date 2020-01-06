FROM library/debian:jessie
MAINTAINER David Villote <dvillote@xtec.cat>
# Music player
RUN apt-get update && \
apt-get -y upgrade && \
apt-get install -y mplayer wget && \
apt-get clean && apt-get autoclean && \
rm -rf /var/lib/apt/lists/* 
VOLUME musica:/downloads
WORKDIR /downloads
ENTRYPOINT [ "mplayer","http://www.tannerhelland.com/dmusic/AMemoryAway.ogg" ]
