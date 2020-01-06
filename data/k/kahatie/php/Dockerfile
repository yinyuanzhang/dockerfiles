FROM kahatie/debian:wheezy
MAINTAINER kahatie <kahatie@gmail.com>

# Volume home
VOLUME ["/home/"]

# Mise a jour / installation des packet
RUN apt-get update && apt-get install -y\
 apache2\
 libapache2-mod-php5\
 php5\
 php5-gd\
 php5-mysql\
 php5-dev\
 php-pear\
 && apt-get clean\
 && rm -rf /var/lib/apt/lists/*

# Copie le fichier de config de supervisord
COPY supervisord.conf /etc/supervisor/conf.d/apache.conf

# Map port 80 et ssl apache2
EXPOSE 80 443
