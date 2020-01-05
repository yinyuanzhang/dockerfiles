FROM brumbrum/php-phantomjs
MAINTAINER Alessandro Lattao <alessandro.lattao@brumbrum.it>

RUN \
  apt-get -y --no-install-recommends install curl vim php-xdebug wget mysql-client imagemagick exiftool php7.0-gd php7.0-imagick gphoto2 iw rfkill iproute2 wpasupplicant isc-dhcp-client ghostscript && \
  mkdir -p /var/run/php && \
  apt-get -y autoclean && \
  apt-get -y clean && \
  apt-get -y autoremove

# Configuro XDebug fpm e cli
ADD /etc/php/7.0/fpm/conf.d/20-xdebug.ini /etc/php/7.0/fpm/conf.d/20-xdebug.ini
ADD /etc/php/7.0/cli/conf.d/20-xdebug.ini /etc/php/7.0/cli/conf.d/20-xdebug.ini

ENV PHP_IDE_CONFIG serverName=docker

# Installo docker-compose (https://github.com/docker/compose/releases)
RUN \
  curl -L https://github.com/docker/compose/releases/download/1.23.2/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose && \
  chmod +x /usr/local/bin/docker-compose

# Installo SonarQube Scanner
# https://docs.sonarqube.org/display/SCAN/Analyzing+with+SonarQube+Scanner#AnalyzingwithSonarQubeScanner-Installation
RUN \
  wget https://binaries.sonarsource.com/Distribution/sonar-scanner-cli/sonar-scanner-cli-3.3.0.1492-linux.zip && \
  unzip sonar-scanner-cli-3.3.0.1492-linux.zip -d /opt/ && \
  echo 'export PATH=$PATH:/opt/sonar-scanner-3.3.0.1492-linux/bin' >> ~/.bashrc && \
  rm sonar-scanner-cli-3.3.0.1492-linux.zip

# Configuro php-fpm
RUN rm /etc/php/7.0/fpm/pool.d/www.conf
ADD /etc/php/7.0/fpm/pool.d/www.conf /etc/php/7.0/fpm/pool.d/www.conf

# FIX DEI PERMESSI IN SCRITTURA/LETTURA PER L'UTENTE WWW-DATA
# A volte il gruppo principale per l'utente locale potrebbe essere differente da 1000
# (ad esempio un secondo o terzo utente creato), per verificare usate il comando "id -g"
RUN usermod -u 1000 www-data

ENTRYPOINT ["/entrypoint.sh"]
