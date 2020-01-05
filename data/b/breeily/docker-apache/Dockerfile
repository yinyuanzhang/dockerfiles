FROM debian:stretch-slim
RUN apt update -y && apt install apache2 wget libapache2-mod-php7.0 php-mysql unzip php-redis -y && \
	wget https://es.wordpress.org/wordpress-5.0.3-es_ES.zip -O /tmp/wordpress-5.0.3-es_ES.zip && \
	unzip /tmp/wordpress-5.0.3-es_ES.zip && \
	mv wordpress/* /var/www/html/ && \
	mv /var/www/html/index.html /var/www/html/index.html.bkp && \
	ln -sf /dev/stdout /var/log/apache2/access.log && \
	ln -sf /dev/stdout /var/log/apache2/error.log && \
	sed -i "s/^session.save_handler.*/session.save_handler = redis/" /etc/php/7.0/apache2/php.ini && \
	sed -i "/^session.save_handler/i session.save_path = \"tcp://redis\"" /etc/php/7.0/apache2/php.ini

ENTRYPOINT ["/usr/sbin/apache2ctl"]
CMD ["-DFOREGROUND"]
EXPOSE 80
