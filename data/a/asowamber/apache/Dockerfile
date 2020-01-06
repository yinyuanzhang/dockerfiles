FROM ubuntu:14.04
MAINTAINER arun@crybit.com
RUN apt-get update -y && apt-get upgrade -y
RUN apt-get install -y apache2
RUN apt-get install -y curl
RUN apt-get install -y ldap-utils
RUN a2enmod authnz_ldap
RUN a2enmod auth_digest
RUN a2enmod proxy
RUN a2enmod proxy_http
RUN a2enmod ssl
COPY authentication.conf /etc/apache2/sites-available/000-default.conf
COPY ws-basic-ng-rec-beb.exp.reseau.sncf.fr.key /etc/ssl/ws-basic-ng-rec-beb.exp.reseau.sncf.fr/ws-basic-ng-rec-beb.exp.reseau.sncf.fr.key
COPY ws-basic-ng-rec-beb.exp.reseau.sncf.fr.cer /etc/ssl/ws-basic-ng-rec-beb.exp.reseau.sncf.fr/ws-basic-ng-rec-beb.exp.reseau.sncf.fr.cer
COPY certificat-racine.cer /etc/ssl/ws-basic-ng-rec-beb.exp.reseau.sncf.fr/certificat-racine.cer
COPY certificat-intermediaire.cer /etc/ssl/ws-basic-ng-rec-beb.exp.reseau.sncf.fr/certificat-intermediaire.cer
EXPOSE 443
CMD ["apache2ctl", "-D", "FOREGROUND"]
