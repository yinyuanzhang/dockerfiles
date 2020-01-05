FROM centos:7

# Set our our meta data for this container.
LABEL name="Linux Production and Development Docker Container"
LABEL description="A Docker Container for development and production Drupal 8, PHP 7 and Perl webapps."
LABEL author="Michael R. Bagnall <mbagnall@itcon-inc.com>"
LABEL vendor="ITCON Services"
LABEL version="1.2"

# Set up our standard binary paths.
ENV PATH /usr/local/src/vendor/bin/:/usr/local/rvm/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin

# Set TERM env to avoid mysql client error message "TERM environment variable not set" when running from inside the container
ENV TERM xterm

# Fix command line compile issue with bundler.
ENV LC_ALL en_US.utf8

# Install and enable repositories
RUN yum -y update && \
  yum -y install epel-release && \
  yum -y install http://rpms.remirepo.net/enterprise/remi-release-7.rpm && \
  rpm -Uvh https://centos7.iuscommunity.org/ius-release.rpm && \
  yum -y update && \
  yum -y install yum-utils && \
  curl -sL https://rpm.nodesource.com/setup_10.x | bash -

RUN yum -y groupinstall "Development Tools" && \
  yum -y install \
  git \
  mariadb \
  wget \
  which \
  gd-devel.x86_64 \
  perl-App-cpanminus.noarch \
  cronie.x86_64 \
  mod_ssl.x86_64 \
  gettext \
  docker \
  bzip2 \
  gcc \
  gcc-c++ \
  make \
  nodejs \
  logrotate \
  webalizer

# Install PHP modules
RUN yum-config-manager --enable remi-php72 && \
  yum -y install \
    php \
    php-bcmath \
    php-curl \
    php-gd \
    php-imap \
    php-mbstring \
    php-mysqlnd \
    php-pgsql \
    php-odbc \
    php-pear \
    php-pecl-imagick \
    php-opcache \
    php-pecl-memcached \
    php-xml \
    php-pecl-redis \
    php-pecl-ssh2 \
    php-pecl-xdebug \
    php-ldap && \
  yum -y install php72-php-pecl-mcrypt.x86_64 && \
  yum -y upgrade && \
  yum clean all

# Install Composer and Drush
RUN curl -sS https://getcomposer.org/installer | php -- \
    --install-dir=/usr/local/bin \
    --filename=composer \
    --version=1.8.6 && \
    composer \
    --working-dir=/usr/local/src/ \
    global \
    require \
    drush/drush:9.* && \
    ln -s /usr/local/src/vendor/bin/drush /usr/bin/drush9 && \
    composer \
    --working-dir=/usr/src/ \
    global \
    require \
    drush/drush:8.* && \
    ln -s /usr/src/vendor/bin/drush /usr/bin/drush8 && \
    ln -s /usr/local/src/vendor/bin/drush /usr/local/bin/drush

RUN curl https://drupalconsole.com/installer -L -o /drupal.phar && \
  mv /drupal.phar /bin/drupal && \
  chmod 755 /bin/drupal

RUN rm -rf /var/www/html && \
  yum -y install sqlite-devel ruby-devel \
  && gem install mailcatcher

COPY etc/httpd/conf/httpd-auth.conf /etc/httpd/conf/httpd-auth.conf
COPY etc/httpd/conf/httpd-noauth.conf /etc/httpd/conf/httpd-noauth.conf
COPY etc/php.ini /etc/php.ini
COPY etc/webalizer.conf /etc/webalizer.conf
COPY etc/sysconfig/webalizer /etc/sysconfig/webalizer

# Our startup script used to install Drupal (if configured) and start Apache.
ADD conf/run-httpd.sh /run-httpd.sh
RUN chmod -v +x /run-httpd.sh

VOLUME ["/var/www/html"]
EXPOSE 80 443

CMD ["/run-httpd.sh"]
