# Tryton stack
#
# This image includes the following tools
# - SIME BEF 2.8
# - QGIS
# - R
#
# Version 1.0

FROM pobsteta/docker-base
MAINTAINER Pascal Obstetar <pascal.obstetar@bioecoforests.com>

# ---------- DEBUT --------------

# On évite les messages debconf
ENV DEBIAN_FRONTEND noninteractive

# Ajoute gosub pour faciliter les actions en root
ENV GOSU_VERSION 1.7
RUN set -x \
	&& apt-get update && apt-get install -y --no-install-recommends ca-certificates wget && rm -rf /var/lib/apt/lists/* \
	&& wget -O /usr/local/bin/gosu "https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$(dpkg --print-architecture)" \
	&& wget -O /usr/local/bin/gosu.asc "https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$(dpkg --print-architecture).asc" \
	&& export GNUPGHOME="$(mktemp -d)" \
	&& gpg --keyserver ha.pool.sks-keyservers.net --recv-keys B42F6819007F00F88E364FD4036A9C25BF357DD4 \
	&& gpg --batch --verify /usr/local/bin/gosu.asc /usr/local/bin/gosu \
	&& rm -r "$GNUPGHOME" /usr/local/bin/gosu.asc \
	&& chmod +x /usr/local/bin/gosu \
	&& gosu nobody true \
	&& apt-get purge -y --auto-remove ca-certificates

# On ajoute le dépôt QGIS
RUN echo "deb http://qgis.org/debian trusty main" > /etc/apt/sources.list.d/qgis.list
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-key 3FF5FFCAD71472C4

# On ajoute le dépôt R
RUN echo "deb http://cran.irsn.fr/bin/linux/ubuntu trusty/" > /etc/apt/sources.list.d/rcran.list
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E084DAB9

# On met à jour
RUN apt-get -y update

# On installe les dépendances de PostgreSQL, Tryton, R et QGIS
# Pour QGIS, R, Tryton
RUN apt-get install -y python-dev python-pip python-lxml python-relatorio python-genshi python-dateutil python-polib python-sql python-psycopg2 python-webdav python-pydot unoconv python-sphinx python-simplejson python-yaml git libgdal1h python-software-properties software-properties-common libpq-dev python-ldap python-gdal python-rpy2 libgeos-dev python-vobject python-vatnumber apache2 qgis qgis-server libapache2-mod-fcgid

## On ajoute l'utilisateur par défaut tryton pour l'installation des librairies R
# On ajoute l'utilisateur tryton au système
RUN useradd --system tryton

# On ajoute le groupe www-data à root pour QGIS-server
RUN addgroup www-data root

# Expose le port 80 pour Apache
EXPOSE 80

# Ajoute les fichiers de conf d'apache
ADD apache.conf /etc/apache2/sites-enabled/000-default.conf
ADD fcgid.conf /etc/apache2/mods-available/fcgid.conf
ADD fqdn.conf /etc/apache2/conf-available/fqdn.conf

# Active fqdn.conf pour éviter le message d'erreur au lancement du serveur apache en localhost
RUN sudo a2enconf fqdn

# On ajoute les librairies "sp" et "rgeos" nécessaire à QGIS, R et Tryton
RUN echo 'install.packages(c("sp", "rgeos"), repos="http://cran.us.r-project.org", dependencies=TRUE)' > /tmp/packages.R \
    && Rscript /tmp/packages.R   

# On ajoute les modules SIME de Bio Eco Forests
ADD ./tryton.tar.gz /opt/

# On ajoute python-dbgis
COPY ./dbgis-0.2.tar.gz /tmp/
RUN pip install /tmp/dbgis-0.2.tar.gz
RUN rm /tmp/dbgis-0.2.tar.gz

# On crée les répertoires nécessaires
RUN mkdir -p /var/lib/tryton
RUN chmod 700 /var/lib/tryton
RUN mkdir -p /var/log/tryton
RUN chmod 700 /var/log/tryton

# On ajoute les VOLUMES
VOLUME ["/var/lib/tryton", "/var/log/tryton"]

# Expose le port 8000 pour Tryton
EXPOSE 8000

# Expose le port 8001 pour QGIS server et http
EXPOSE 8001

# On lance apache en tâche de fond
CMD ["apache2ctl", "-D", "FOREGROUND"]

# ---------- FIN --------------
#
# Nettoie les APT
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/*
