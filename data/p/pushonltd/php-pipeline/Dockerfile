FROM php:7.0-cli-alpine

MAINTAINER Rhys Botfield <rhys@pushon.co.uk>

ENV _BUILD_DEPS \
        libpng-dev \
        jpeg-dev \
        freetype-dev \
        icu-dev \
        libmcrypt-dev \
        libxml2-dev \
        libxslt-dev

RUN apk add --no-cache libpng \
        libjpeg-turbo \
        freetype \
        icu \
        libmcrypt \
        libxslt \
        ${_BUILD_DEPS} \
    && docker-php-ext-configure gd --with-png-dir=/usr --with-jpeg-dir=/usr --with-freetype-dir=/usr \
    && docker-php-ext-install gd pdo_mysql soap xsl mysqli intl bcmath zip mcrypt \
    && apk del ${_BUILD_DEPS}

# PECL extensions
RUN apk add --no-cache ${PHPIZE_DEPS} \
    && pecl install -o -f redis \
    && docker-php-ext-enable redis \
    && apk del ${PHPIZE_DEPS}

RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer \
    && composer global require hirak/prestissimo

# Ioncube
RUN curl -o ioncube_loaders_lin_x86-64.tar.gz http://downloads3.ioncube.com/loader_downloads/ioncube_loaders_lin_x86-64.tar.gz \
    && tar xfz ioncube_loaders_lin_x86-64.tar.gz \
    && cp ioncube/ioncube_loader_lin_7.0.so /usr/local/lib/php/extensions/no-debug-non-zts-20151012/ \
    && echo "zend_extension=ioncube_loader_lin_7.0.so" > /usr/local/etc/php/conf.d/00_docker-php-ext-ioncube_loader_lin_7.0.ini \
    && rm -Rf ioncube_loaders_lin_x86-64.tar.gz ioncube

#Build Node v8 from source
ENV NODE_VERSION 8.15.1
RUN apk add --no-cache libstdc++ \
    && apk add --no-cache --virtual .node-build-deps \
        binutils-gold \
        curl \
        g++ \
        gcc \
        gnupg \
        libgcc \
        linux-headers \
        make \
        python \
	&& for key in \
		94AE36675C464D64BAFA68DD7434390BDBE9B9C5 \
		FD3A5288F042B6850C66B31F09FE44734EB7990E \
		71DCFD284A79C3B38668286BC97EC7A07EDE3FC1 \
		DD8F2338BAE7501E3DD5AC78C273792F7D83545D \
		C4F0DFFF4E8C1A8236409D08E73BC641CC11F4C8 \
		B9AE9905FFD7803F25714661B63B535A4C206CA9 \
		56730D5401028683275BD23C23EFEFE93C4CFFFE \
		77984A986EBC2AA786BC0F66B01FBB92821C587A \
		8FCCA13FEF1D0C2E91008E09770F7A9A5AE15600 \
	; do \
		gpg --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys "$key" || \
		gpg --keyserver hkp://ipv4.pool.sks-keyservers.net --recv-keys "$key" || \
		gpg --keyserver hkp://pgp.mit.edu:80 --recv-keys "$key" ; \
	done \
    && curl -fsSLO --compressed "https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION.tar.xz" \
    && curl -fsSLO --compressed "https://nodejs.org/dist/v$NODE_VERSION/SHASUMS256.txt.asc" \
    && gpg --batch --decrypt --output SHASUMS256.txt SHASUMS256.txt.asc \
    && grep " node-v$NODE_VERSION.tar.xz\$" SHASUMS256.txt | sha256sum -c - \
    && tar -xf "node-v$NODE_VERSION.tar.xz" \
    && cd "node-v$NODE_VERSION" \
    && ./configure \
    && make -j$(getconf _NPROCESSORS_ONLN) \
    && make install \
    && apk del .node-build-deps \
    && cd .. \
    && rm -Rf "node-v$NODE_VERSION" \
    && rm "node-v$NODE_VERSION.tar.xz" SHASUMS256.txt.asc SHASUMS256.txt

# Install global npm decendencies
RUN npm install --global --no-package-lock yarn  \
    && npm install --global --no-package-lock gulp-cli \
    && npm install --global --no-package-lock grunt-cli \
    && npm install --global --no-package-lock bower  \
    && echo '{ "allow_root": true }' > /root/.bowerrc

# Install some misc linux tools used in deployments
RUN apk add --no-cache git openssh-client rsync patch
