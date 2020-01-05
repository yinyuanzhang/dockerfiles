FROM ubuntu:16.04
MAINTAINER Carlos Ardilles R-1.0.18 <carlos@prefeituramoderna.com.br>
MAINTAINER Alberto Matos <alberto@prefeituramoderna.com.br>
ENV TZ 'America/Sao_Paulo'
RUN echo $TZ > /etc/timezone && \
    apt-get update && apt -y upgrade && apt-get install -y tzdata && \
    rm /etc/localtime && \
    ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && \
    dpkg-reconfigure -f noninteractive tzdata
RUN apt install -y apache2 apache2-bin apache2-data apache2-utils libapache2-mod-php libpq5 libcurl4-openssl-dev curl libcurl3-gnutls libcurl3 libbz2-dev libjpeg62 libjpeg62-dev libltdl-dev 
RUN apt install -y libmcrypt-dev libmcrypt4  libpng12-0 libpng12-dev libsnmp-base libsnmp-dev libtidy-dev libxml2 libxml2-dev libxmp-dev libxslt1-dev  libzip-dev 
RUN apt install -y php php-cli  php-common php-composer-semver php-fpm php-imagick php-mbstring php-pgsql php-gd php-xml php-zip zlib1g-dev php-curl php-dev php-mcrypt 
COPY php.ini /etc/php/7.0/apache2/
COPY security.conf /etc/apache2/conf-available/
COPY 000-default.conf /etc/apache2/sites-available/
COPY manager_application_server_module.conf /etc/apache2/mods-available/
COPY manager_application_server_module.load /etc/apache2/mods-available/
COPY manager_application_server_module.so /usr/lib/apache2/modules/
COPY api_integracaogeo_server_module.conf /etc/apache2/mods-available/
COPY api_integracaogeo_server_module.load /etc/apache2/mods-available/
COPY api_integracaogeo_server_module.so /usr/lib/apache2/modules/
COPY api_integracaogeoteste_server_module.conf /etc/apache2/mods-available/
COPY api_integracaogeoteste_server_module.load /etc/apache2/mods-available/
COPY api_integracaogeoteste_server_module.so /usr/lib/apache2/modules/
RUN apt-get -y autoremove
RUN apt-get clean
RUN ln -s /usr/lib/x86_64-linux-gnu/libpq.so.5 /usr/lib/x86_64-linux-gnu/libpq.so
RUN a2enmod manager_application_server_module
RUN a2enmod api_integracaogeo_server_module
RUN a2enmod api_integracaogeoteste_server_module
RUN a2enmod rewrite
RUN a2enmod php7.0
RUN sed -i "s/short_open_tag = Off/short_open_tag = On/" /etc/php/7.0/apache2/php.ini
RUN sed -i "s/UTF-8/ISO-8859-1/" /etc/php/7.0/apache2/php.ini
ENV APACHE_RUN_USER www-data
ENV APACHE_RUN_GROUP www-data
ENV APACHE_LOG_DIR /var/log/apache2
ENV APACHE_LOCK_DIR /var/lock/apache2
ENV APACHE_PID_FILE /var/run/apache2.pid
EXPOSE 80
CMD /usr/sbin/apache2ctl -DFOREGROUND
