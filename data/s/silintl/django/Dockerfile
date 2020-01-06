FROM silintl/apache2:latest
MAINTAINER "Phillip Shipley" <phillip_shipley@sil.org>

ENV REFRESHED_AT 2015-08-19

# Install Django packages
RUN apt-get update -y \
	&& apt-get install -y \
        curl \
        libapache2-mod-wsgi \
        python-dateutil \
        python-mysqldb \
        python-setuptools  \
        rsyslog-gnutls \
    && easy_install pip \
    && pip install django==1.4.20 \
    && curl -o /usr/local/bin/whenavail https://bitbucket.org/silintl/docker-whenavail/raw/master/whenavail \
    && chmod a+x /usr/local/bin/whenavail

EXPOSE 80
CMD ["apache2ctl", "-D", "FOREGROUND"]
