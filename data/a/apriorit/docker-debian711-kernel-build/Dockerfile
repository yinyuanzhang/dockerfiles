FROM debian:7.11

RUN  /bin/sed -i -- 's/#deb-src/deb-src/g' /etc/apt/sources.list \
	&& /bin/sed -i -- 's/# deb-src/deb-src/g' /etc/apt/sources.list \
	&& apt-get update
RUN apt-get -y 	install	apt-utils

RUN apt-get -y 	install \
                fakeroot \
                build-essential \
                ncurses-dev \
                xz-utils \
                libssl-dev \
                bc \
                flex \
                libelf-dev \
                bison \
                crash \
                kexec-tools \
                makedumpfile \
                kernel-wedge

RUN apt-get -y 	install \
                git \
                libncurses5-dev \
                libelf-dev \
                asciidoc \
                binutils-dev \
		packaging-dev
