FROM ubuntu:18.04
LABEL maintainer aizat125

RUN apt-get update && \
	apt-get install python -y && \
	apt-get install wget -y && \
	apt-get install lsof -y && \
	apt-get install zip -y && \
	apt-get install xvfb -y && \
	apt-get install imagemagick -y && \
	mkdir /startup-script

RUN	wget -nv -O- https://download.calibre-ebook.com/linux-installer.sh | sh /dev/stdin

COPY start.sh /startup-script

RUN	chmod 777 /startup-script/start.sh && \
	apt-get clean && \
	rm -rf /var/cache/apt/* /var/lib/apt/lists/*

COPY calibre /srv/calibre

EXPOSE 8080

CMD ["bash" , "./startup-script/start.sh"]