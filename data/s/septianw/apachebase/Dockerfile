FROM ailispaw/ubuntu-essential:16.04-nodoc
#FROM septianw/essloc:16.04

ENV DEBIAN_FRONTEND=noninteractive
ENV APACHE_RUN_USER=www-data
ENV APACHE_RUN_GROUP=www-data
RUN apt-get update && apt-get upgrade -y && apt-get install -y locales && locale-gen en_US.UTF-8
ENV LANG=en_US.UTF-8
RUN apt-get update && apt-get -y -q install apache2 php7.0 libapache2-mod-php7.0 && apt-get purge -y software-properties-common locales && apt-get autoremove -y && rm -r /var/cache/apt /var/lib/apt/lists && rm -f /var/log/apache2/error.log /var/log/apache2/access.log &&  ln -s /dev/stderr /var/log/apache2/error.log && ln -s /dev/stdout /var/log/apache2/access.log

ADD default-override.conf /etc/apache2/conf-available/default-override.conf
ADD php.ini /etc/php/7.0/apache2/php.ini
ADD entrypoint.sh /entrypoint.sh
ADD envvars /etc/apache2/envvars
RUN chmod 700 /entrypoint.sh && \
    a2enconf default-override && \
    a2enmod rewrite && a2enmod headers && a2enmod expires && \
    update-rc.d apache2 disable

EXPOSE 80
VOLUME ["/var/log/"]
CMD /entrypoint.sh
