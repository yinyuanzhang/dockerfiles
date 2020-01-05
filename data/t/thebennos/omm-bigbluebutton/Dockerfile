FROM ubuntu:14.04
MAINTAINER Benjamin Wenderoth <b.wenderoth@gmail.com>

RUN apt-get -y update
RUN apt-get install -y language-pack-en vim wget
RUN update-locale LANG=en_US.UTF-8
RUN dpkg-reconfigure locales
# Making Sure that multiverse is set
#Add multiverse repo
RUN echo "deb http://us.archive.ubuntu.com/ubuntu/ trusty multiverse" | tee -a /etc/apt/sources.list
RUN apt-get -y update
RUN apt-get -y dist-upgrade

#Install PPA for LibreOffice 4.4 and libsslAnchor link for: install ppa for libreoffice 44 and libssl
RUN apt-get install -y software-properties-common
RUN add-apt-repository ppa:libreoffice/libreoffice-4-4
RUN add-apt-repository -y ppa:ondrej/php
#Install key for BigBlueButtonAnchor link for: install key for bigbluebutton
RUN wget http://ubuntu.bigbluebutton.org/bigbluebutton.asc -O- | apt-key add -
RUN echo "deb http://ubuntu.bigbluebutton.org/trusty-1-0/ bigbluebutton-trusty main" | tee /etc/apt/sources.list.d/bigbluebutton.list
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 4F4EA0AAE5267A6C
RUN apt-get -y update

#Install ffmpegAnchor link for: install ffmpeg
RUN apt-get install -y libvpx1 libvorbisenc2 build-essential git-core checkinstall yasm texi2html libvorbis-dev libx11-dev libvpx-dev libxfixes-dev zlib1g-dev pkg-config netcat libncurses5-dev
ADD install-ffmpeg.sh .
RUN chmod +x install-ffmpeg.sh
RUN ./install-ffmpeg.sh
RUN ffmpeg -version
RUN apt-get install -y libpam-systemd policykit-1 colord policykit-1-gnome

# Install BBB magic
RUN apt-get install -y bigbluebutton
RUN apt-get install -y bbb-config bbb-demo bbb-check haveged

EXPOSE 80 9123 1935
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*