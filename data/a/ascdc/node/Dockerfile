FROM ubuntu:xenial
MAINTAINER ASCDC <ascdc.sinica@gmail.com>

ENV LANG zh_TW.UTF-8
ENV LANGUAGE zh_TW
ENV LC_ALL zh_TW.UTF-8
ENV AUTHORIZED_KEYS **None**

RUN mkdir /script

ADD locale.gen /etc/locale.gen
ADD locale-archive /usr/lib/locale/locale-archive
ADD set_root_pw.sh /script/set_root_pw.sh
ADD run.sh /script/run.sh	

RUN DEBIAN_FRONTEND=noninteractive && \
	chmod +x /script/*.sh && \
	echo "cd /script" >> /root/.profile && \
	echo "alias ll='ls -al'" >> /root/.profile && \
	apt-get -qq update && \
	apt-get -y -qq dist-upgrade && \
	apt-get -y -qq install locales openssh-server pwgen vim wget curl screen sudo git python2.7 make build-essential pkg-config cmake libblkid-dev e2fslibs-dev libboost-all-dev libaudit-dev  libgdk-pixbuf2.0-dev netcat iputils-ping net-tools jq && \
	locale-gen zh_TW && \
	locale-gen zh_TW.UTF-8 && \
	dpkg-reconfigure --frontend=noninteractive locales && \ 
	update-locale LANG="zh_TW.UTF-8" LANGUAGE="zh_TW" && \
	echo "export LANG=zh_TW.UTF-8" >> /root/.profile && \ 
	echo "export LANGUAGE=zh_TW" >> /root/.profile && \
	echo "export LC_ALL=zh_TW.UTF-8" >> /root/.profile && \
	mkdir -p /var/run/sshd && \
	sed -i "s/UsePrivilegeSeparation.*/UsePrivilegeSeparation no/g" /etc/ssh/sshd_config && \
	sed -i "s/UsePAM.*/UsePAM no/g" /etc/ssh/sshd_config && \
	sed -i "s/PermitRootLogin.*/PermitRootLogin yes/g" /etc/ssh/sshd_config && \
	curl -sL https://deb.nodesource.com/setup_8.x | sudo -E bash - && \
	apt-get -qq update && \
	apt-get -y -qq install nodejs && \
	npm install -g node-gyp && \ 
	apt-get install libcurl4-openssl-dev -y && \
	wget http://curl.haxx.se/download/curl-7.58.0.tar.gz && tar zxvf curl-7.58.0.tar.gz && cd curl-7.58.0 && ./configure && make && make install && ldconfig

WORKDIR /script
EXPOSE 22
ENTRYPOINT ["/script/run.sh"]
