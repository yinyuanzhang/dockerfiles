FROM php:cli

RUN apt update && \
	apt -fy install --no-install-recommends \
	locales \
	sendmail \
	#libxml2-dev \
	libglib2.0-dev \
	libmdbsql2 \
	mdbtools \
	mdbtools-dbg \
	mdbtools-dev \
	#mdbtools-gmd \
	odbc-mdbtools \
	gzip \
	libpq-dev \
	# postgresql-dev \
	# php-pgsql \
	# php-pdo-pgsql \
	unixodbc \
	unixodbc-dev && \
	rm -rf /var/lib/apt/lists/*

ENV LANG pt_BR.UTF-8
ENV LANGUAGE pt_BR
ENV LC_ALL pt_BR.UTF-8
RUN locale-gen pt_BR.UTF-8
RUN ln -s /etc/locale.alias /usr/share/locale/locale.alias
RUN sed -i -e 's/# pt_BR.UTF-8 UTF-8/pt_BR.UTF-8 UTF-8/' /etc/locale.gen
RUN dpkg-reconfigure --frontend=noninteractive locales
RUN update-locale LANG=pt_BR.UTF-8 LANGUAGE=pt_BR
RUN dpkg-reconfigure --frontend=noninteractive locales

ENV TZ America/Sao_Paulo
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN dpkg-reconfigure -f noninteractive tzdata

RUN docker-php-ext-configure mbstring
RUN set -x \
	&& cd /usr/src/php/ext/odbc \
	&& phpize \
	&& sed -ri 's@^ *test +"\$PHP_.*" *= *"no" *&& *PHP_.*=yes *$@#&@g' configure \
	&& ./configure --with-unixODBC=shared,/usr \
	&& docker-php-ext-install \
	odbc \
	pdo \
	pdo_pgsql \
	pgsql

RUN echo 'sendmail_path = "/usr/sbin/sendmail -t -i"' > /usr/local/etc/php/conf.d/mail.ini

RUN echo 'alias cl="clear && ls -lhtFA"' >> ~/.bashrc
RUN echo 'alias cls="clear && ls"' >> ~/.bashrc