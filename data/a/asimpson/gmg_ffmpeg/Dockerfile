FROM ubuntu:14.04
MAINTAINER Adam Simpson <asimpson@grahamdigital.com>

# install packages
RUN echo America/Detroit > /etc/timezone && dpkg-reconfigure --frontend noninteractive tzdata
RUN echo deb http://archive.ubuntu.com/ubuntu precise universe multiverse >> /etc/apt/sources.list
RUN apt-get update
RUN apt-get -y upgrade
RUN apt-get -y install autoconf automake build-essential git libfaad-dev libbz2-dev libass-dev libgpac-dev libtheora-dev libtool libvdpau-dev libvorbis-dev pkg-config texi2html zlib1g-dev libmp3lame-dev wget; apt-get clean
RUN apt-get -y install nginx

# grab sources
#RUN git clone git://git.videolan.org/x264.git /usr/local/src/x264
#RUN git clone git://github.com/mstorsjo/fdk-aac.git /usr/local/src/fdk-aac
#RUN git clone https://chromium.googlesource.com/webm/libvpx /usr/local/src/libvpx
#RUN git clone git://source.ffmpeg.org/ffmpeg /usr/local/src/ffmpeg
#RUN wget http://downloads.xiph.org/releases/opus/opus-1.0.3.tar.gz -P  /usr/local/src
#RUN wget http://www.tortall.net/projects/yasm/releases/yasm-1.2.0.tar.gz -P  /usr/local/src

# YASM build
RUN wget http://www.tortall.net/projects/yasm/releases/yasm-1.2.0.tar.gz -P /usr/local/src
RUN cd /usr/local/src; tar xzvf yasm-1.2.0.tar.gz; cd yasm-1.2.0; ./configure; make -j 4; make install; make distclean;

# libx264 build
RUN git clone git://git.videolan.org/x264.git /usr/local/src/x264
RUN cd /usr/local/src/x264; ./configure --enable-static; make -j 4; make install; make distclean

# libfdk-aac build
RUN git clone git://github.com/mstorsjo/fdk-aac.git /usr/local/src/fdk-aac
RUN cd /usr/local/src/fdk-aac; autoreconf -fiv; ./configure --disable-shared; make -j 4; make install; make distclean

# libvpx build
RUN git clone https://chromium.googlesource.com/webm/libvpx /usr/local/src/libvpx
RUN cd /usr/local/src/libvpx; ./configure --disable-examples; make -j 4; make install; make clean

# libopus build
RUN wget http://downloads.xiph.org/releases/opus/opus-1.0.3.tar.gz -P /usr/local/src
RUN cd /usr/local/src; tar zxvf opus-1.0.3.tar.gz; cd opus-1.0.3; ./configure --disable-shared; make -j 4; make install; make distclean

# ffmpeg build
RUN git clone git://source.ffmpeg.org/ffmpeg /usr/local/src/ffmpeg
RUN cd /usr/local/src/ffmpeg; ./configure --extra-libs="-ldl" --enable-gpl --enable-libass --enable-libfdk-aac --enable-libmp3lame --enable-libopus --enable-libtheora --enable-libvorbis --enable-libvpx --enable-libx264 --enable-nonfree; make -j 4; make install; make distclean; hash -r

WORKDIR /usr/share/nginx/html
EXPOSE 80:8888
