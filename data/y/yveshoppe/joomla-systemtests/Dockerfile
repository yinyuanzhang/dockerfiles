# Joomla! System tests - Build 2016-08-16
FROM ubuntu:xenial
MAINTAINER Yves Hoppe <yves@compojoom.com>

# Set correct environment variables.
ENV HOME /root

# update the package sources
RUN apt-get update -qq

# we use the enviroment variable to stop debconf from asking questions..
RUN DEBIAN_FRONTEND='noninteractive' apt-get install -y mysql-server apache2 mysql-client php7.0 \
  php7.0-cli php7.0-curl php7.0-gd php7.0-mysql php7.0-zip php7.0-xml php7.0-mbstring libapache2-mod-php7.0 curl \
	wget unzip git fluxbox firefox openjdk-8-jre xvfb \
	dbus libasound2 libqt4-dbus libqt4-network libqtcore4 libqtgui4 libpython2.7 libqt4-xml libaudio2 fontconfig nodejs npm

# package install is finished, clean up
RUN apt-get clean # && rm -rf /var/lib/apt/lists/*

# Create testing directory
RUN mkdir -p /tests/www

# Apache site conf
ADD config/000-default.conf /etc/apache2/sites-available/000-default.conf

# clean up tmp files (we don't need them for the image)
RUN rm -rf /tmp/* /var/tmp/*

# Composer
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=bin --filename=composer
RUN composer self-update

# Start Apache and MySQL
CMD /usr/bin/mysqld_safe & apache2ctl -D FOREGROUND
