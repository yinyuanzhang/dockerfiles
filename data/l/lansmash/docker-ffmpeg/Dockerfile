FROM ubuntu:latest
#FROM debian:latest


# debian updates
RUN apt-get update && apt-get upgrade -y && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

ENV DOCKERFFMPEG_VERSION 1

#COPY decklink /root/ffmpeg_sources/decklink


# ffmpeg libraries and compilers including desktop video driver tools
#RUN apt-get update && apt-get -y install autoconf automake build-essential libass-dev libfreetype6-dev \
#   libtheora-dev libtool libvorbis-dev \
#   pkg-config texinfo wget zlib1g-dev \
#   yasm checkinstall git libmp3lame-dev dkms libgl1-mesa-glx libgl1 linux-headers-amd64 && \
#apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \

# ffmpeg libraries and compilers
RUN apt-get update && apt-get -y install autoconf automake build-essential libfreetype6-dev \
   libtheora-dev libtool libvorbis-dev \
   pkg-config texinfo wget zlib1g-dev \
   yasm checkinstall git libmp3lame-dev unzip && \
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \


mkdir -p ~/ffmpeg_sources && \

# compile nasm 2.13
cd ~/ffmpeg_sources && \
wget http://www.nasm.us/pub/nasm/releasebuilds/2.13.01/nasm-2.13.01.tar.bz2 && \
tar xjvf nasm-2.13.01.tar.bz2 && \
cd nasm-2.13.01 && \
./autogen.sh && \
./configure && make && checkinstall -y && \

# compile latest libx264
cd ~/ffmpeg_sources && \
git clone git://git.videolan.org/x264.git && \
cd x264 && ./configure --enable-static && \
make && checkinstall -y --pkgversion 0 && ldconfig && \
cp /root/ffmpeg_sources/x264/*.deb /root && \

cd ~/ffmpeg_sources && \
git clone https://github.com/mstorsjo/fdk-aac.git && \
cd fdk-aac && ./autogen.sh && ./configure --enable-static && \
make && checkinstall -y --pkgversion 0 && ldconfig && \

mkdir /usr/local/share/doc && mkdir /usr/local/share/ffmpeg && \

cd ~/ffmpeg_sources && \
wget -O decklink.zip https://www.dropbox.com/s/hqjuxvthmc8n5i3/bm-include.zip?dl=1 && \
mkdir -p decklink && \
unzip -j decklink.zip -d decklink && \

# compile latest ffmpeg
cd ~/ffmpeg_sources && \
git clone http://source.ffmpeg.org/git/ffmpeg.git && \
cd ~/ffmpeg_sources/ffmpeg && \
./configure --enable-gpl --enable-libx264 \
  --enable-static \
  --enable-libfdk-aac \
  --enable-libmp3lame \
  --extra-cflags=-I../decklink --extra-ldflags=-I../decklink \
  --enable-decklink \
  --pkg-config-flags="--static" \
  --enable-nonfree && \
make && checkinstall -y && ldconfig && \
ffmpeg -h && echo hi && \

cp /root/ffmpeg_sources/ffmpeg/*.deb /root && \ 


SUDO_FORCE_REMOVE=yes apt-get -y --autoremove purge nasm \
  autoconf automake build-essential  \
  libtheora-dev libtool libvorbis-dev \
  pkg-config texinfo wget zlib1g-dev \
  yasm checkinstall git && \
 #libgl1-mesa-glx libgl1 linux-headers-amd64 unzip && \
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \
rm -rf ~/ffmpeg_sources && \

ffmpeg -h && echo finished

#EXPOSE 53/udp 53/tcp 953/tcp
#VOLUME ["/etc/bind"]
#VOLUME ["/var/lib/bind"]

COPY entrypoint.sh /sbin/entrypoint.sh
RUN chmod 755 /sbin/entrypoint.sh
#ENTRYPOINT ["/sbin/entrypoint.sh"]

