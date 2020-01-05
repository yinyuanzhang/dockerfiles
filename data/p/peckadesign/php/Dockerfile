FROM peckadesign/php:7.4

RUN docker-php-ext-install \
	exif

RUN apt-get update -y \
	&& apt-get install -y --no-install-recommends \
	imagemagick \
	&& apt-get clean -y \
	&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
