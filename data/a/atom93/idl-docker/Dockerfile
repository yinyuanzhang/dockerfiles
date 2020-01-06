FROM ubuntu:16.04

SHELL ["/bin/bash","-c"]

RUN apt-get update && \
	apt-get install -y wget && \
	wget http://cloud.recas.ba.infn.it:8080/v1/AUTH_fb6d6fcd0e194a96bb6d0420dce8332f/backgroundinfo/idl85envi53sp1linux.x86_64.tar.gz && \
	gunzip idl85envi53sp1linux.x86_64.tar.gz && \
	tar -xf idl85envi53sp1linux.x86_64.tar && \
	bash install.sh -s < /silent/idl_answer_file && \
	echo "export PATH=$PATH:/usr/local/exelis/idl85/bin" >> /etc/bash.bashrc && \
	wget ftp.us.debian.org/debian/pool/main/libx/libxp/libxp6_1.0.2-2_amd64.deb && \
	apt install -y ./libxp6_1.0.2-2_amd64.deb && \
	apt-get -f install && \
	apt-get install -y libfreetype6 && \
	apt-get install -y libxmu6 && \
	apt-get install -y libxpm4 && \
	apt-get install -y vnc4server && \
	printf "password\npassword\n\n" | vncpasswd && \
	apt-get install -y xautomation






