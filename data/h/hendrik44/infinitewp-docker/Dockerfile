FROM php:7.2-apache

RUN apt-get update && apt-get install -y unzip

RUN docker-php-ext-install mysqli

RUN set -ex; \
	curl -o infinitewp.zip -fSL "https://infinitewp.com/iwp-admin-panel-download.php";

RUN set -ex; \
		unzip -a infinitewp.zip; \
		rm infinitewp.zip; \
		cd */; \
		chown -R www-data:www-data . ; \
		iwpPath=$(pwd); \ 
		mv * ../ ; \
		cd .. && rm -rf $iwpPath;

RUN apt-get clean && apt-get autoremove