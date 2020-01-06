FROM ascdc/apache2-php56
MAINTAINER ASCDC <asdc.sinica@gmail.com>

ADD run.sh /run.sh

RUN DEBIAN_FRONTEND=noninteractive && \
	chmod +x /*.sh && \
	apt-get update && \
	apt-get -y install sshpass

EXPOSE 80
WORKDIR /var/www/html
ENTRYPOINT ["/run.sh"]
