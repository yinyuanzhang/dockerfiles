FROM ajoergensen/baseimage-ubuntu

RUN \
	apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF && \
	echo "deb http://download.mono-project.com/repo/ubuntu bionic main" > /etc/apt/sources.list.d/mono-official.list && \
        apt-get -q update && \
	apt-get -qy --force-yes dist-upgrade && \
	apt-get -y install mono-complete ca-certificates-mono libcurl3 && \
	/usr/local/sbin/cleanup.sh
