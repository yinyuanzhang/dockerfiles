# Docker Image Builder v2
#
# These images are built using Dockerfile inheritance to build the images used for Probo.CI.
#
# Image: proboci/ubuntu
# Tag: 18.04
# 
# The default Node.js version is 8.x in Ubuntu 18.04. 
# The npm package is also required for Ubuntu 18.04.
#
# Build the proboci/ubuntu:18.04 image:tag with the following command from inside the src/ubuntu/18.04 directory where the Dockerfile lives:
# docker build -t proboci/ubuntu:18.04

# Set our our meta data for this container.

FROM ubuntu:18.04

LABEL name="Ubuntu 18.04 LTS Based ProboCI Image"
LABEL description="Our base container for ProboCI Builds."
LABEL author="Michael R. Bagnall <mrbagnall@icloud.com>"
LABEL vendor="ProboCI, LLC."

WORKDIR /root

ENV TERM xterm

# Update apt repos and install base apt packages.
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y apt-utils \
  apt-transport-https \
  build-essential \
  ca-certificates \
  curl \
  git \
  gnupg \
  libnss3 \
  lsb-release \
  memcached \
  nano \
  netcat-openbsd \
  nodejs \
  ntp \
  openjdk-8-jre \
  redis-server \
  sendmail \
  software-properties-common \
  sudo \
  vim \
  wget \
  zip

# Install apt packages for LAMP, npm, ruby, and all other tools available from apt.
COPY files/mysql-setup.sql /mysql-setup.sql
COPY files/mycnf.txt /root/.my.cnf
COPY files/varnishcache_varnish41.list /etc/apt/sources.list.d/varnishcache_varnish41.list
RUN curl -L https://packagecloud.io/varnishcache/varnish41/gpgkey | sudo apt-key add - \
  && wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | APT_KEY_DONT_WARN_ON_DANGEROUS_USAGE=DontWarn apt-key add - \
  && echo 'deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main' | tee /etc/apt/sources.list.d/google-chrome.list \
  && add-apt-repository ppa:ondrej/php \
  && apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y php7.2 \
  php7.2-bcmath \
  php7.2-bz2 \
  php7.2-cli \
  php7.2-common \
  php7.2-curl \
  php7.2-dba \
  php7.2-dev \
  php7.2-gd \
  php7.2-json \
  php7.2-ldap \
  php7.2-mbstring \
  php7.2-mysql \
  php7.2-opcache \
  php7.2-readline \
  php7.2-soap \
  php7.2-xml \
  php7.2-zip \
  php7.2-pgsql \
  php-memcached \
  libapache2-mod-php7.2 \
  php-redis \
  php-imagick \
  php-pear \
  imagemagick \
  postgresql \
  postgresql-contrib \
  apache2 \
  apache2-utils \
  mysql-server \
  mysql-client \
  google-chrome-stable \
  libreadline-dev \
  zlib1g-dev \
  ruby-dev \
  libsqlite3-dev \
  varnish/xenial \
  && service mysql start \
  && mysql -uroot < /mysql-setup.sql \
  && rm -rf /tmp/* /mysql-setup.sql

# Install Composer and Drush
RUN curl -sS https://getcomposer.org/installer | php -- \
  --install-dir=/usr/local/bin \
  --filename=composer \
  --version=1.8.5 \
  && composer \
  --working-dir=/usr/local/src/ \
  global \
  require \
  drush/drush:8.* \
  && ln -s /usr/local/src/vendor/bin/drush /usr/local/bin/drush

# Download Drupal Console and install it in our standard path.
RUN curl https://drupalconsole.com/installer -L -o /tmp/drupal.phar \
  && mv /tmp/drupal.phar /usr/local/bin/drupal \
  && chmod +x /usr/local/bin/drupal

# Get Node Package Manager
RUN apt-get install -y npm

# Install NPM packages and setup proboscis.
# The proboscis package is required!
RUN npm install -g bower \
  grunt-cli \
  gulp-cli \
  lighthouse \
  the-a11y-machine \
  yarn \
  proboscis \
  --no-document \
  && ln -s /usr/lib/node_modules/proboscis/bin/proboscis /usr/bin/proboscis \
  && ln -s /usr/lib/node_modules/proboscis/bin/proboscis-control /usr/bin/proboscis-control \
  && ln -s /usr/lib/node_modules/proboscis/bin/proboscis-format /usr/bin/proboscis-format \
  && rm -rf /var/lib/apt/lists/* /tmp/*

# Start and configure our PostgreSQL server.
COPY files/pgpass.txt /root/.pgpass
RUN service postgresql start \
  && su - postgres -c "createuser -d -l -r -s root" \
  && su - postgres -c "createdb --owner=postgres drupal" \
  && psql --username=root --dbname=drupal -c "ALTER USER root WITH PASSWORD 'strongpassword';" \
  && chmod 0600 /root/.pgpass \
  && service postgresql stop

# Configure Apache. Be sure to enable apache mods or you're going to have a bad time.
RUN rm -rf /var/www/html \
  && a2enmod rewrite \
  && a2enmod actions \
  && a2enmod alias \
  && a2enmod deflate \
  && a2enmod dir \
  && a2enmod expires \
  && a2enmod headers \
  && a2enmod mime \
  && a2enmod negotiation \
  && a2enmod setenvif \
  && a2enmod proxy \
  && a2enmod proxy_http
COPY files/apache-default-host.conf /etc/apache2/conf-enabled/apache-default-host.conf

# Install Ruby and Gem packages.
RUN gem install rails \
  mailcatcher \
  compass \
  bundler \
  --no-document

# Install solr with default search cores.
RUN wget http://archive.apache.org/dist/lucene/solr/6.6.5/solr-6.6.5.tgz \
  && tar xzf solr-6.6.5.tgz solr-6.6.5/bin/install_solr_service.sh --strip-components=2 \
  && ./install_solr_service.sh solr-6.6.5.tgz  \
  && wget https://ftp.drupal.org/files/projects/search_api_solr-7.x-1.14.tar.gz \
  && tar xzf search_api_solr-7.x-1.14.tar.gz \
  && mv search_api_solr /opt/solr/. \
  && sudo -u solr -- /opt/solr/bin/solr create -c drupal7 -d "/opt/solr/search_api_solr/solr-conf/6.x" \
  && wget https://ftp.drupal.org/files/projects/search_api_solr-8.x-2.3.tar.gz \
  && rm -rf /opt/solr/search_api_solr \
  && tar xzf search_api_solr-8.x-2.3.tar.gz \
  && mv search_api_solr /opt/solr/. \
  && sudo -u solr -- /opt/solr/bin/solr create -c drupal8 -d "/opt/solr/search_api_solr/solr-conf/6.x" \
  && service solr stop

# Install varnish default configs.
COPY files/wordpress-default-4.vcl /etc/varnish/wordpress-default-4.vcl
COPY files/drupal-default-4.vcl /etc/varnish/default.vcl
COPY files/varnish /etc/default/varnish
COPY files/secret /etc/varnish/secret

# Create .ssh dir and add SSH config file.
# TODO: There's got to be a better way to setup the /root/.ssh/config file. Using old method for now.
RUN mkdir /root/.ssh \
  && chmod 700 /root/.ssh \
  && touch /root/.ssh/config \
  && chmod 0700 /root/.ssh/config \
  && echo "Host *" >> /root/.ssh/config \
  && echo "StrictHostKeyChecking no" >> /root/.ssh/config

# Install WP-CLI Wordpress command line tool, https://wp-cli.org/.
RUN curl -o /tmp/wp-cli.phar https://raw.githubusercontent.com/wp-cli/builds/gh-pages/phar/wp-cli.phar \
  && chmod +x /tmp/wp-cli.phar \
  && mv /tmp/wp-cli.phar /usr/local/bin/wp
