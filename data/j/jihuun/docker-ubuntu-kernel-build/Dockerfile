FROM		ubuntu:16.04
MAINTAINER	jihuun.k@gmail.com

# Install dependencies
RUN		apt-get -y -q update \
		&& apt-get install -y -q \
		git gcc vim cscope exuberant-ctags wget make \
		bc bison flex grep gawk gperf gettext ccache xz-utils \
		libncurses-dev libncurses5-dev libssl-dev \
		mutt \
#		binutils-arm-linux-gnueabihf \
#		gcc-arm-linux-gnueabihf \
#		gccgo-4.7-arm-linux-gnueabi \
		gcc-aarch64-linux-gnu \
		u-boot-tools \
		libelf-dev \
		build-essential kernel-package fakeroot

RUN		git clone https://github.com/scriptworld/cscope-filter
