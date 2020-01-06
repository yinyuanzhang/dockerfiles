FROM wordpress:4.9.8-php7.2

LABEL vendor="Gavia Online"
LABEL maintainer="Docker Team <docker@ubiquos.io>"


# Install PHP extensions
RUN apt-get update && \
    apt-get upgrade -qy && \
    apt-get install --no-install-recommends -y \
      cron \
      git \
      wget \
      libc-client-dev \
      libicu-dev \
      libkrb5-dev \
      libmcrypt-dev \
      libssl-dev \
      libz-dev \
      unzip \
      zip \
      nginx \
      nano \
      sudo \
      libgeoip-dev \
      libmemcached-dev \
      zlib1g-dev \
      systemd\
      libjpeg-dev \
  		libpng-dev \
      libtidy-dev \
      libbz2-dev \
      curl \
      libcurl4-openssl-dev \
      libedit-dev \
      libxml2-dev


RUN apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false && \
    rm -rf /var/lib/apt/lists/* && \
    rm /etc/cron.daily/*

RUN docker-php-ext-configure imap --with-imap --with-imap-ssl --with-kerberos && \
    docker-php-ext-configure gd --with-png-dir=/usr --with-jpeg-dir=/usr && \
    docker-php-ext-install imap intl mbstring mysqli pdo_mysql zip gd opcache tidy bcmath bz2 curl exif json phar simplexml soap xml xmlrpc && \
    docker-php-ext-enable imap intl mbstring mysqli pdo_mysql zip gd opcache tidy bcmath bz2 curl exif json phar simplexml soap xml xmlrpc

RUN pecl install memcached && \
    docker-php-ext-enable memcached

RUN pecl install redis && \
    pecl install xdebug && \
    pecl install igbinary && \
    pecl install APCu &&\
    # pecl install geoip && \
    docker-php-ext-enable redis xdebug apcu igbinary


#################
# Deploy Wordpress #
#################

# Define Mautic version and expected SHA1 signature
# ENV WORDPRESS_VERSION 4.9.9
# ENV WORDPRESS_SHA1 10678608e8b7f373ca906c8966c09faffe27e5ae


# Setting envirotment variables
# ENV WORDPRESS_DB_NAME 					"mycubanmarket-db"
# ENV WORDPRESS_DB_HOST 					"mycubanmarket-mariadb"
# ENV WORDPRESS_TABLE_PREFIX 			"mcm_"
# ENV WORDPRESS_DB_PASSWORD 			"lamisma10*+-"
# ENV WORDPRESS_LOGGED_IN_SALT 		"4tKf+hDbkIk#O9C4PxuHlo7JFM5l4!$_,>(tQb%d+WQ|yxlI7sQk#F?ui9ATbQ.+"
# ENV WORDPRESS_LOGGED_IN_KEY 		"#H7rBY#lCTy4weB1o?TL,w@g;<el[0un?oUx`au-MbrExaQr Z>2 {i3+X+:9MVB"
# ENV WORDPRESS_SECURE_AUTH_SALT 	"Q$K-kDjo(h|aOit>/-wLb=OyC[n,cS,IEikJEHa6$ke:f~,/[inX8LIqa|acX0?X"
# ENV WORDPRESS_SECURE_AUTH_KEY 	"KrauC045{;B5lYgQ];h+l]y5lo}NP@IP%-otJ+{lO`X^+8xpKl8n/;cP)+ivx-<9"
# ENV WORDPRESS_NONCE_SALT 				"gTE]:m;eL 7$%7!H|qg_MMDqvQrW/[gT%%(8WOr=EW$7qN+}ldf;<(aJ!1LG>|e)"
# ENV WORDPRESS_NONCE_KEY 				"5D?6Lr}`2)^pvEK`x>_kKs9(J9AB]*T|GKM]CHVNb|DnJg%mDh#Goi#dkCA<?QO+"
# ENV WORDPRESS_AUTH_SALT 				":mI<D{-RmLm</Vd>QfohmY^$|yeZV++w,|c<,4r10D;O/`ztyu~kvv,r+vzb1+L-"
# ENV WORDPRESS_AUTH_KEY 					".%t%5_a.Dm2kvk84BN|vxIwM0$SUEeB:%hQWZU^>U)QpCTG4/4-O+!]33-tRt<<Q'"
# ENV WORDPRESS_DEBUG							"true"


# WORKDIR /var/www/html


# Download package and extract to web volume
# RUN set -ex; \
# 		curl -o wordpress.tar.gz -fSL "https://wordpress.org/wordpress-${WORDPRESS_VERSION}.tar.gz"; \
# 		echo "$WORDPRESS_SHA1 *wordpress.tar.gz" | sha1sum -c -; \
# 		# upstream tarballs include ./wordpress/ so this gives us /usr/src/wordpress
# 		tar -xzf wordpress.tar.gz -C /usr/src/; \
# 		rm wordpress.tar.gz; \
# 		chown -R www-data:www-data /usr/src/wordpress
#
#
#
# COPY wordpress-original-entrypoint.sh /
#
# COPY entrypoint.sh /
#
# COPY wordpress-nginx.conf /etc/nginx/conf.d/wordpress-nginx.conf
#
# RUN sudo chmod +x /wordpress-original-entrypoint.sh
# RUN sudo chmod +x /entrypoint.sh
#
# RUN service nginx start
#
# ENTRYPOINT ["/wordpress-original-entrypoint.sh"]
#
# CMD ["php-fpm"]



#ENTRYPOINT /entrypoint.sh /wordpress-original-entrypoint.sh
