FROM ubuntu:xenial
LABEL maintainer "Pascal Martineau <pascal@lewebsimple.ca>"

# Install package dependencies
RUN echo "deb http://ppa.launchpad.net/ondrej/php/ubuntu xenial main" > /etc/apt/sources.list.d/ondrej-php-xenial.list \
  && echo "deb-src http://ppa.launchpad.net/ondrej/php/ubuntu xenial main" >> /etc/apt/sources.list.d/ondrej-php-xenial.list \
  && apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E5267A6C \
  && apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
  apache2 \
  build-essential \
  ca-certificates \
  curl \
  git \
  less \
  imagemagick \
  iputils-ping \
  language-pack-fr-base \
  msmtp \
  nano \
  openssh-client \
  php \
  php-cli \
  php-curl \
  php-dev \
  php-gd \
  php-intl \
  php-mbstring \
  php-mysql \
  php-xml \
  php-zip \
  php-pear \
  php-xdebug \
  rsync \
  tzdata \
  wget \
  && rm -rf /var/lib/apt/lists/*

# Default Apache2 UID
ENV APACHE_UID 1000

# Copy configuration files
COPY config/ /

# Set timezone
RUN ln -sf /usr/share/zoneinfo/America/Toronto /etc/localtime

# Configure Apache2
RUN set -ex \

  # Load Apache environment variables
  && . /etc/apache2/envvars \

  # Configure server (FQDN / robots)
  && a2enconf fqdn robots \

  # Enable Apache modules
  && a2enmod expires headers rewrite vhost_alias \
  && apache2ctl graceful \

  # Disable Indexes in default vhost
  && sed -e '/Options Indexes FollowSymLinks/ s/^#*/#/' -i /etc/apache2/apache2.conf \

  # Remove SSL vhost configuration
  && rm /etc/apache2/sites-available/default-ssl.conf \

  # Enable vhosts configuration
  && a2ensite vhosts \

  # Output error log to stderr
  && ln -sfT /dev/stderr "${APACHE_LOG_DIR}/error.log" \
  && ln -sfT /dev/stdout "${APACHE_LOG_DIR}/access.log" \

  # Install Xdebug with pecl
  && pecl install xdebug \

  # Create Xdebug directory
  && mkdir -p /tmp/xdebug \

  # Change UID/GID of www-data to match local user
  && usermod --non-unique --uid ${APACHE_UID} www-data \
  && groupmod --non-unique --gid ${APACHE_UID} www-data \

  # Adjust directory permissions
  && chown -R www-data:www-data /var/www /tmp \

  # Generate fr_CA locale
  && locale-gen fr_CA.utf8

# Install ionCube
RUN wget http://downloads3.ioncube.com/loader_downloads/ioncube_loaders_lin_x86-64.tar.gz \
  && tar xvfz ioncube_loaders_lin_x86-64.tar.gz \
  && cp ioncube/ioncube_loader_lin_7.3.so /usr/lib/php/7.3/ \
  && rm ioncube_loaders_lin_x86-64.tar.gz

# Install Node.js 10.x
RUN curl -sL https://deb.nodesource.com/setup_10.x | bash - \
  && apt-get install -y nodejs \
  && rm -rf /var/lib/apt/lists/*

VOLUME ["/var/www/html","/tmp"]
WORKDIR /var/www/html

EXPOSE 80

CMD ["/docker-entrypoint.sh"]
