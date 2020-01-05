FROM ubuntu:xenial

ENV DEBIAN_FRONTEND noninteractive
ENV VGNUCASH=2.6.18
ENV RGNUCASH=2.6.18-1

ADD startup.sh /startup.sh
RUN chmod 0755 /startup.sh && \
	mkdir /var/gnucash

#Setup Language
RUN apt-get update && apt-get install -y locales && \
	locale-gen de_DE en_US en_GB 

#Install packages
WORKDIR /opt
RUN apt-get update -y && \
	apt-get install -y git x11vnc xvfb openbox net-tools python-numpy menu &&  \
	git clone https://github.com/kanaka/noVNC.git noVNC && \
	git clone https://github.com/kanaka/websockify noVNC/utils/websockify && \
	apt-get remove -y git && \
	apt-get autoremove -y && \
	apt-get autoclean -y && \
	rm -rf /var/lib/apt/lists/*

#Install GnuCash from Source
WORKDIR /tmp/build/gnucash
RUN apt-get update -y && \
	apt-get build-dep -y gnucash && \
	apt-get purge -y guile-2.0 && \
	apt-get install -y \
		wget slib libgnomeui-common libgnomeui-dev guile-1.8 guile-1.8-dev checkinstall \
		build-essential autoconf intltool libtool \
		aqbanking-tools && \
	wget "https://downloads.sourceforge.net/project/gnucash/gnucash (stable)/$VGNUCASH/gnucash-$RGNUCASH.tar.bz2" && \
	tar xvjf gnucash-$RGNUCASH.tar.bz2 && rm gnucash-$RGNUCASH.tar.bz2 && mv gnucash-$VGNUCASH/* . && rmdir gnucash-$VGNUCASH && \
	./configure --enable-compile-warnings --with-html-engine=webkit --enable-aqbanking && \
	make && make install && checkinstall -y && ldconfig && \
	rm -r /tmp/build && \
	apt-get remove -y \
		wget slib libgnomeui-common libgnomeui-dev guile-1.8-dev checkinstall \
		build-essential autoconf intltool libtool && \
	apt-get autoremove -y && \
	apt-get autoclean -y && \
	rm -rf /var/lib/apt/lists/*

#Setup Volumes
VOLUME /var/gnucash

#Finalize
WORKDIR /var/gnucash
CMD /startup.sh
EXPOSE 6080
