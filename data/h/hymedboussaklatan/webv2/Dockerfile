FROM ubuntu:latest

RUN apt update && apt upgrade -y && DEBIAN_FRONTEND=noninteractive apt install -y apache2 php php-mysql nano 
RUN a2enmod ssl

COPY WEB/seed-it.eu.conf /etc/apache2/sites-available
COPY WEB/seed-it.eu.connexion.conf /etc/apache2/sites-available
COPY WEB/seed-it.eu.inscription.conf /etc/apache2/sites-available

RUN ln -s /etc/apache2/sites-available/seed-it.eu.conf /etc/apache2/sites-enabled
RUN ln -s /etc/apache2/sites-available/seed-it.eu.connexion.conf /etc/apache2/sites-enabled
RUN ln -s /etc/apache2/sites-available/seed-it.eu.inscription.conf /etc/apache2/sites-enabled


RUN mkdir /var/www/seed-it.eu
RUN mkdir /var/www/seed-it.eu/css
RUN mkdir /var/www/seed-it.eu/images

RUN mkdir /var/www/seed-it.eu.connexion
RUN mkdir /var/www/seed-it.eu.connexion/css

RUN mkdir /var/www/seed-it.eu.inscription
RUN mkdir /var/www/seed-it.eu.inscription/css


COPY WEB/acceuil/index.html /var/www/seed-it.eu/index.html
COPY WEB/acceuil/css/default.css /var/www/seed-it.eu/css
COPY WEB/acceuil/images/seed.png /var/www/seed-it.eu/images
COPY WEB/acceuil/images/seed-it-logo.png /var/www/seed-it.eu/images
COPY WEB/acceuil/images/Raspberrypi.png /var/www/seed-it.eu/images

COPY WEB/connexion/signIn.html /var/www/seed-it.eu.connexion/index.html
COPY WEB/connexion/css/signIn.css /var/www/seed-it.eu.connexion/css

COPY WEB/connexion/signUp.html /var/www/seed-it.eu.inscription/index.html
COPY WEB/connexion/css/signUp.css /var/www/seed-it.eu.inscription/css

EXPOSE 80 443

CMD apachectl -DFOREGROUND
