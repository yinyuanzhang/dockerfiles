FROM ubuntu:18.04
LABEL maintainer "oliver.krebs@me.com"
LABEL Description="McMyAdmin"
LABEL Vendor="olikre"
LABEL Version="1.0"

ENV JAVA_MEMORY=2048

EXPOSE	8080
EXPOSE	25565

ARG DEBIAN_FRONTEND="noninteractive"

RUN	apt-get update && \
	apt-get -y upgrade && \
	apt-get -y install wget openjdk-8-jdk-headless unzip libgdiplus && \
	apt-get clean && \
	rm -rf /var/lib/apt/lists/* 
		
WORKDIR	/usr/local
RUN	wget http://mcmyadmin.com/Downloads/etc.zip && \
	unzip etc.zip && rm etc.zip

WORKDIR	/home/mcmyadmin
RUN	wget http://mcmyadmin.com/Downloads/MCMA2_glibc26_2.zip && \
	unzip MCMA2_glibc26_2.zip && rm MCMA2_glibc26_2.zip

RUN mkdir /home/mcmyadmin/Minecraft && \
    echo 'eula=true' > /home/mcmyadmin/Minecraft/eula.txt

RUN echo '#!/bin/sh' > /start.sh && \
    echo '/home/mcmyadmin/MCMA2_Linux_x86_64 +java.memory $JAVA_MEMORY' >> /start.sh

RUN	chmod 755 /start.sh

RUN touch /home/mcmyadmin/McMyAdmin.conf
RUN	/home/mcmyadmin/MCMA2_Linux_x86_64 -nonotice -updateonly 
RUN	/home/mcmyadmin/MCMA2_Linux_x86_64 -configonly -setpass admin 

VOLUME /home/mcmyadmin

CMD	["/start.sh"]
