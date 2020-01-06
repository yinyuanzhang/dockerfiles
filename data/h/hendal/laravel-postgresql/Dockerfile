FROM webdevops/php-apache:7.2
#  default-jre
RUN apt update && apt install -y libpq-dev libxrender1 libfontconfig1 libx11-dev libjpeg62 libxtst6 \
    && docker-php-ext-configure pgsql -with-pgsql=/usr/local/pgsql \
    && docker-php-ext-install pdo pdo_pgsql pgsql \
    && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
