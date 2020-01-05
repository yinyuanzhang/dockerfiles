FROM eboraas/apache-php
MAINTAINER Christoph Auer <auer.chrisi@gmx.net>

ADD configure.sh /configure.sh

RUN /usr/sbin/a2enmod rewrite
RUN apt-get update && apt-get -y install mcrypt php5-mcrypt php5-curl && apt-get clean && rm -r /var/lib/apt/lists/*

# Enable mcrypt
RUN php5enmod mcrypt

# Disable directory listing
RUN /usr/sbin/a2dismod -f autoindex

# Disable server signatures
RUN echo "ServerSignature Off" >> /etc/apache2/apache2.conf
RUN echo "ServerTokens Prod" >> /etc/apache2/apache2.conf

CMD ["/configure.sh"]
