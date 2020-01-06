FROM debian:8.7
MAINTAINER Sergey Izgiyaev <sergo27@gmail.com>

ENV DEBIAN_FRONTEND=noninteractive \
    POWERADMIN_VERSION=2.1.7 \
    APACHE_RUN_USER=www-data \
    APACHE_RUN_GROUP=www-data \
    APACHE_LOG_DIR=/var/log/apache2

RUN apt-get update && apt-get install --no-install-recommends --no-install-suggests wget ca-certificates \
                                        apache2 php5 php5-mysql libapache2-mod-php5 php5-mcrypt netcat \
                                        -y && \
    wget -O /tmp/poweradmin.tgz https://netix.dl.sourceforge.net/project/poweradmin/poweradmin-${POWERADMIN_VERSION}.tgz && \
    tar zxf /tmp/poweradmin.tgz -C /tmp && \
    rm /var/www/html/index.html && \
    mv /tmp/poweradmin-${POWERADMIN_VERSION}/* /var/www/html/ && \
    rm -Rf /tmp/poweradmin* && \
    apt-get purge wget ca-certificates -y && \
    apt-get autoremove -y -qq && \
	apt-get clean -qq && \
	rm -rf /var/lib/apt/lists/* && \
    rm -Rf /var/www/html/install

RUN /usr/sbin/a2dismod 'mpm_*' && \
    /usr/sbin/a2enmod mpm_prefork 
    ##### TO ADD SSL SUPPORT LATER
    # && \
    #/usr/sbin/a2ensite default-ssl
    #/usr/sbin/a2enmod ssl

COPY ./add_mysql_tables.php /
COPY ./poweradmin_mysql.sql /

COPY ./entrypoint.sh /bin/
RUN chmod +x /bin/entrypoint.sh

STOPSIGNAL SIGTERM

ENTRYPOINT ["entrypoint.sh"]
