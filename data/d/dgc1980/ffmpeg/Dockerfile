## ffmpeg docker to enable use of mscorefonts

FROM jrottenberg/ffmpeg:4.1-ubuntu

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update
RUN apt-get install -y --no-install-recommends software-properties-common curl apt-transport-https
RUN apt-add-repository multiverse
RUN apt-get update

RUN echo "ttf-mscorefonts-installer msttcorefonts/accepted-mscorefonts-eula select true" | debconf-set-selections
RUN echo "ttf-mscorefonts-installer msttcorefonts/present-mscorefonts-eula note" | debconf-set-selections

RUN apt-get install -y --no-install-recommends fontconfig ttf-mscorefonts-installer msttcorefonts
RUN fc-cache -f -v
