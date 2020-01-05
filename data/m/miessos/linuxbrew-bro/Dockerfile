FROM debian:jessie

MAINTAINER miessos, https://github.com/miessos

# Set the path
ENV DEBIAN_FRONTEND noninteractive
RUN echo 'export PKG_CONFIG_PATH=/usr/local/lib/pkgconfig:/usr/local/lib64/pkgconfig:/usr/lib64/pkgconfig:/usr/lib/pkgconfig:/usr/lib/x86_64-linux-gnu/pkgconfig:/usr/lib64/pkgconfig:/usr/share/pkgconfig:$PKG_CONFIG_PATH' >> /root/.profile
RUN echo '## Setup linux brew' >> /root/.profile
RUN echo 'export LINUXBREWHOME=$HOME/.linuxbrew' >> /root/.profile
RUN echo 'export PATH=$LINUXBREWHOME/bin:$PATH' >> /root/.profile
RUN echo 'export MANPATH=$LINUXBREWHOME/man:$MANPATH' >> /root/.profile
RUN echo 'export PKG_CONFIG_PATH=$LINUXBREWHOME/lib64/pkgconfig:$LINUXBREWHOME/lib/pkgconfig:$PKG_CONFIG_PATH' >> /root/.profile
RUN echo 'export LD_LIBRARY_PATH=$LINUXBREWHOME/lib64:$LINUXBREWHOME/lib:$LD_LIBRARY_PATH' >> /root/.profile

# Install dependencies
RUN apt-get update && apt-get install -y build-essential \
make \
cmake \
scons \
curl \
git \
ruby \
autoconf \
automake \
autoconf-archive \                               
gettext \
libtool \
flex \
bison \                               
libbz2-dev \
libcurl4-openssl-dev \
libexpat-dev \
libncurses-dev \
libpcap-dev

# Clone linuxbrew
RUN git clone https://github.com/Homebrew/linuxbrew.git ~/.linuxbrew

# Update brew and install bro
RUN /bin/bash --login -c "brew update"
RUN /bin/bash --login -c "brew install bro"

RUN cd ~
