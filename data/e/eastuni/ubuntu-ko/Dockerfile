FROM eastuni/ubuntu-ko:18.04

# Apache ENVs
ENV APACHE_RUN_USER www-data
ENV APACHE_RUN_GROUP www-data
ENV APACHE_LOCK_DIR /var/lock/apache2
ENV APACHE_LOG_DIR /var/log/apache2
ENV APACHE_PID_FILE /var/run/apache2/apache2.pid
ENV APACHE_SERVER_NAME localhost

RUN apt-get update \
 && apt-get install -y software-properties-common \
 && apt-get update \
 && add-apt-repository ppa:ondrej/apache2 \
 && apt-get update \
 && apt-get install -y apache2 \
 && rm -rf /var/lib/apt/lists/* \
 && a2enmod proxy && a2enmod proxy_http	&& a2enmod proxy_html

# Expose Apache
EXPOSE 80

# Launch Apache
CMD ["/usr/sbin/apache2ctl", "-DFOREGROUND"]
