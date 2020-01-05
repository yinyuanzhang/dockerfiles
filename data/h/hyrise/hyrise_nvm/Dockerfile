FROM ubuntu:14.04
MAINTAINER Marvin Keller <marv@ramv.de>

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && apt-get install -y \
		autoconf \
		binutils-dev \
		build-essential \
		bzip2 \
		ccache \
		cmake \
		curl \
		doxygen \
		flex \
		gcc-multilib \
		gdb \
		gfortran \
		git \
		htop \
		libboost-all-dev \
		libev-dev \
		libgoogle-perftools-dev \
		libhwloc-dev \
		liblog4cxx10 \
		liblog4cxx10-dev \
		libmetis-dev \
		libmysqlclient-dev \
		libpapi-dev \
		libtbb-dev \
		libtool \
		libunwind8-dev \
		man \
		mysql-server \
		nano \
		nodejs-legacy \
		npm \
		python \
		python-pip \
		screen \
		strace \
		sudo \
		tcpdump \
		telnet \
		vim \
		wget \
	&& apt-get clean \
	&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*


ENV tmpDir /tmp/hyrise
RUN mkdir $tmpDir

WORKDIR $tmpDir

RUN wget http://downloads.sourceforge.net/project/libcsv/libcsv/libcsv-3.0.1/libcsv-3.0.1.tar.gz; \
	tar -xf libcsv-3.0.1.tar.gz; \
	cd $tmpDir/libcsv-3.0.1; \
	make install -j 4;

WORKDIR /tmp
RUN rm -rf $tmpDir

# Set up my user
RUN useradd hyrise -u 1000 -s /bin/bash -m \
	&& gpasswd -a hyrise sudo \
	&& echo 'hyrise:hyrise123' | chpasswd

RUN locale-gen en_US en_US.UTF-8
RUN dpkg-reconfigure locales

WORKDIR /home/hyrise

RUN mkdir -p /home/hyrise/.ssh
RUN ssh-keyscan github.com >> /home/hyrise/.ssh/known_hosts

ADD . /home/hyrise/hyrise_nvm
RUN chown -R hyrise /home/hyrise/

USER hyrise

WORKDIR /home/hyrise/hyrise_nvm

RUN git submodule update --init \
	&& cp makefiles/settings.default.mk settings.mk \
	&& sed -i 's/PERSISTENCY := NONE/PERSISTENCY := BUFFEREDLOGGER/g' settings.mk \
	&& sed -i 's/REPLICATION := 0/REPLICATION := 1/g' settings.mk \
	&& make -j 4 \
	&& find . -not -path './build/hyrise-server_release' -a -not -path './third_party*' -a -not -path './build' -delete


