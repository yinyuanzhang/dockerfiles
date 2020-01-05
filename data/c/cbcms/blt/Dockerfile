# VERSION 2.0
# AUTHOR: Douglas Groene....
# DESCRIPTION: Acquia BLT stack for Drupal 8 Projects.
# BUILD: docker build --rm -t cbcms/blt .
# SOURCE: https://bitbucket.com/cbit/blt

FROM php:7.3

MAINTAINER Doug Groene <dgroene@collegeboard.org>

# Setup environment variables.
ENV SONAR_SCANNER_VERSION=3.0.3.778-linux \
  SONAR_SCANNER_HOME=/opt/sonar-scanner    
RUN apt-get update && apt-get install -y --no-install-recommends apt-utils
RUN mkdir -p /usr/share/man/man1 && \
  apt-get update -y && \
  apt-get install -y openjdk-11-jdk

# Install dependencies
RUN set -ex \
  && apt-get update -yqq \
  && apt-get install -yqq \
  git \
  unzip \
  wget \
  curl \
  rsync \
  libmcrypt-dev \
  libgd-dev \
  libbz2-dev \
  libzip-dev \
  libcurl4-openssl-dev \
  openssh-client \
  libmagickwand-dev \
  default-mysql-client \
  default-libmysqlclient-dev \
  default-jre \
  gnupg \
  ca-certificates \
  apt-transport-https \
  ttf-wqy-zenhei \
  imagemagick \
  procps \
  # Install NodeJS & NPM
  && curl -sL https://deb.nodesource.com/setup_11.x | bash - \
  && apt-get install -y nodejs \
  # Install required PHP extensions.
  && docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ \
  && docker-php-ext-install -j$(nproc) bz2 gd pdo_mysql curl mbstring opcache zip \
  && pecl install xdebug imagick \
  # Install composer
  && curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer \
  # Add composer dependencies
  && composer global require "hirak/prestissimo:^0.3" \
  # Fetch and install sonar scanner
  && curl -fsSLO https://binaries.sonarsource.com/Distribution/sonar-scanner-cli/sonar-scanner-cli-${SONAR_SCANNER_VERSION}.zip \
  && unzip sonar-scanner-cli-${SONAR_SCANNER_VERSION}.zip \
  && mv sonar-scanner-$SONAR_SCANNER_VERSION $SONAR_SCANNER_HOME \
  # Remove zip files
  && rm sonar-scanner-cli-${SONAR_SCANNER_VERSION}.zip \
  # Create symlinks
  && ln -s $SONAR_SCANNER_HOME/bin/sonar-runner /usr/bin/sonar-runner\
  && ln -s $SONAR_SCANNER_HOME/bin/sonar-scanner /usr/bin/sonar-scanner \
  && ln -s $SONAR_SCANNER_HOME/bin/sonar-scanner-debug /usr/bin/sonar-scanner-debug \
  # Remove unwanted packages.
  && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false


CMD ["php", "-a"]