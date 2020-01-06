FROM php:7.2.2-apache-stretch

MAINTAINER admin@yakeworld.top 

RUN apt update \
    && apt -y --no-install-recommends install wget unzip git \        
	#&& wget https://codeload.github.com/Abban/glype/zip/master -O /tmp/glype.zip \
	&& git clone https://github.com/Abban/glype.git /var/www/html \
	&& sed -i '$d' /var/www/html/includes/settings.php \
 	#&& rm /tmp/*.zip \
	&& chown -R www-data:www-data /var/www/html 
