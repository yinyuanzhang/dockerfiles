from smeat/debian:jessie

RUN apt-get update && apt-get -y install apache2 \
	&& apt-get clean && rm -rf /var/lib/apt/lists/*

EXPOSE 80 
EXPOSE 443

CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]
