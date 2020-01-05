FROM linuxconfig/lamp
MAINTAINER Lubos Rendek <web@linuxconfig.org>

# Install prerequisites 
RUN apt-get install -y wget unzip php-zip

# Download and unzip Joomla
RUN wget -O /tmp/joomla.zip https://downloads.joomla.org/cms/joomla3/3-8-12/Joomla_3-8-12-Stable-Full_Package.zip
RUN rm /var/www/html/*
RUN unzip /tmp/joomla.zip  -d /var/www/html/
RUN rm /tmp/joomla.zip

# Create database
RUN service mysql start; mysqladmin -uadmin -ppass create joomla

# Update file ownership
RUN chown -R www-data.www-data /var/www/html

# Apache configuration
ADD 000-default.conf /etc/apache2/sites-available/
RUN a2enmod rewrite

# Joomla configurations
RUN mv /var/www/html/htaccess.txt /var/www/html/.htaccess 

# Allow ports
EXPOSE 80

CMD ["supervisord"]
