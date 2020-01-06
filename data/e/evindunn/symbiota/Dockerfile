FROM debian:stable-slim

ENV DEBIAN_FRONTEND noninteractive

# Don't change these
ENV APACHE_RUN_DIR "/var/run/apache2"
ENV APACHE_PID_FILE "/var/run/apache.pid"
ENV APACHE_RUN_USER "www-data"
ENV APACHE_RUN_GROUP "www-data"
ENV APACHE_LOG_DIR "/var/log/apache2"

ENV SYMBIOTA_ROOT /var/www/symbiota
ENV SYMBIOTA_OVERLAY /var/lib/symbiota

# Install dependencies
RUN apt-get update &&                   \
    apt-get dist-upgrade -y &&          \
    apt-get install -y                  \
        apache2                         \
        git                             \
        imagemagick                     \
        libapache2-mod-php              \
        libyaml-0-2                     \
        php-gd                          \
        php-mbstring                    \
        php-mysql                       \
        php-solr                        \
        php-xml                         \
        php-yaml                        \
        php-zip                         \
        tesseract-ocr &&                \
    apt-get autoremove --purge -y &&    \
    rm -rf /var/lib/apt/lists/*

# Get the source
RUN git clone --depth 1 https://github.com/Symbiota/Symbiota.git ${SYMBIOTA_ROOT}

# Enable php for apache
RUN a2enmod php7.0

# Copy over the yaml/php overlay files
RUN mkdir -p ${SYMBIOTA_OVERLAY}
COPY config/index.php ${SYMBIOTA_OVERLAY}/
COPY config/header.php ${SYMBIOTA_OVERLAY}/
COPY config/footer.php ${SYMBIOTA_OVERLAY}/

RUN mkdir -p ${SYMBIOTA_OVERLAY}/config
COPY config/symbini.php ${SYMBIOTA_OVERLAY}/config/
COPY config/dbconnection.php ${SYMBIOTA_OVERLAY}/config/

RUN /bin/bash -c 'chmod +x ${SYMBIOTA_OVERLAY}/config/{symbini,dbconnection}.php' &&   \
    /bin/bash -c 'chmod +x ${SYMBIOTA_OVERLAY}/{index,header,footer}.php'

# Edit these for custom style
RUN cp -r ${SYMBIOTA_ROOT}/css ${SYMBIOTA_OVERLAY}/ &&                                                  \
    mv ${SYMBIOTA_OVERLAY}/css/main_template.css ${SYMBIOTA_OVERLAY}/css/main.css &&                    \
    mv ${SYMBIOTA_OVERLAY}/css/speciesprofile_template.css ${SYMBIOTA_OVERLAY}/css/speciesprofile.css

# Mount /usr/local/etc/symbiota outside the container to configure symbiota
COPY config/yml/* /usr/local/etc/symbiota/

# Configure apache
RUN sed -i "s/LogLevel warn/LogLevel info/" /etc/apache2/apache2.conf
COPY apache.conf /etc/apache2/sites-available/000-default.conf

RUN sed -Ei "s/upload_max_filesize.*/upload_max_filesize = 10M/" /etc/php/7.0/apache2/php.ini

# Log apache & php output to console
RUN ln -sf /dev/stdout /var/log/apache2/access.log &&   \
    ln -sf /dev/stderr /var/log/apache2/error.log

RUN chmod -R +r ${SYMBIOTA_ROOT}

# Configure volumes
VOLUME /usr/local/etc/symbiota
VOLUME ${SYMBIOTA_ROOT}
VOLUME ${SYMBIOTA_OVERLAY}

# TODO: SSL Support
EXPOSE 80
EXPOSE 443

# Configure entrypoint
COPY docker-entrypoint.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/docker-entrypoint.sh

WORKDIR ${SYMBIOTA_ROOT}
ENTRYPOINT ["docker-entrypoint.sh"]
CMD ["apache2", "-DFOREGROUND"]
