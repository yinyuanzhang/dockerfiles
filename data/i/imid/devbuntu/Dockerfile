FROM ubuntu:16.04

# Install php and apache2
RUN apt-get update && \
	apt-get -y install software-properties-common && \
	LC_ALL=C.UTF-8 add-apt-repository ppa:ondrej/php && \
	LC_ALL=C.UTF-8 add-apt-repository ppa:ondrej/apache2 && \
	apt-get update && \
	apt-get -y install \
 curl wget unzip \
 php7.2 php7.2-cli php7.2-fpm php7.2-common php7.2-bcmath php7.2-curl php7.2-fpm php7.2-gd php7.2-intl php7.2-json php7.2-ldap php7.2-mbstring php7.2-mysql php7.2-odbc php7.2-opcache php7.2-readline php7.2-soap php7.2-sybase php7.2-xml php7.2-xmlrpc php7.2-zip  libapache2-mod-php7.2\
 mariadb-client vim nano\
 imagemagick && \
 a2enmod rewrite rewrite vhost_alias headers

# Custom apache config
COPY apache.conf /etc/apache2/sites-available/000-default.conf
ENV APACHE_DOCUMENT_ROOT /var/www/html # Placeholder, you can change this at runtime

# Create the workdir
RUN mkdir -p /var/www/html
WORKDIR /var/www/html
EXPOSE 80

# Use www-data
ADD www-data.sh /usr/local/bin/w3d
RUN chmod +x /usr/local/bin/w3d

# Let apache run in foreground
COPY apache2-foreground /usr/local/bin/
CMD ["apache2-foreground"]


