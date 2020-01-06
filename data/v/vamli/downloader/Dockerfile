FROM ubuntu:xenial

ARG REPOSITORY_TAG=2.0.3

RUN apt-get update && \
    DEBIAN_FRONTEND="noninteractive" apt-get install -y --no-install-recommends python-software-properties \
    software-properties-common apt-transport-https lsb-release ca-certificates wget cron rsync ssh build-essential git

RUN LC_ALL=C.UTF-8 add-apt-repository -y ppa:ondrej/php && \
    apt-get update -y

RUN DEBIAN_FRONTEND="noninteractive" apt-get install -y --no-install-recommends php7.1 php7.1-fpm php7.1-cli php7.1-curl \
    php7.1-mcrypt php7.1-common php7.1-mbstring php7.1-dom php7.1-xml php7.1-zip php7.1-pdo php7.1-sqlite3 supervisor && \
    DEBIAN_FRONTEND="noninteractive" apt-get install -y --no-install-recommends nginx && \
    apt-get autoremove && apt-get clean && \
    rm -rf "/var/lib/apt/lists/*" && \
    mkdir -p "/var/log/supervisor" && \
    mkdir -p "/data/database" && \
    mkdir -p "/run/php" && \
    php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');" && \
    php -r "if (hash_file('SHA384', 'composer-setup.php') === '93b54496392c062774670ac18b134c3b3a95e5a5e5c8f1a9f115f203b75bf9a129d5daa8ba6a13e2cc8a1da0806388a8') { echo 'Installer verified'; } else { echo 'Installer corrupt'; unlink('composer-setup.php'); } echo PHP_EOL;" && \
    php composer-setup.php && \
    php -r "unlink('composer-setup.php');" && \
    mv composer.phar "/usr/local/bin/composer" && \
    composer global require hirak/prestissimo

RUN mkdir "/var/www/downloader/" && cd "/var/www/downloader" && \
    git clone https://github.com/mkoziy/downloader . && \
    git checkout tags/$REPOSITORY_TAG && \
    composer install && \
    chmod +x artisan && \
    chmod -R 755 "/var/www/downloader/storage/" && \
    php -r "file_exists('/data/database/database.sqlite') || touch('/data/database/database.sqlite');" && \
    ./artisan cache:clear && \
    ./artisan key:generate && \
    chown -R www-data:www-data "/var/www/downloader/storage" && \
    chown -R www-data:www-data "/var/www/downloader/database" && \
    chown -R www-data:www-data "/data/database" && \
    chown -R www-data:www-data "/var/www/downloader/storage/app/ssh_keys" && \
    chown -R www-data:www-data "/var/www/downloader/storage/logs" && \
    echo "* * * * * www-data /var/www/downloader/artisan schedule:run >> /tmp/cron.log" >> "/etc/crontab"

COPY "./build/supervisord.conf" "/etc/supervisor/supervisord.conf"
COPY "./build/host.conf" "/etc/nginx/sites-available/default"

EXPOSE 80 443

CMD ['chown -R www-data:www-data "/var/www/downloader/storage"']
CMD ['chown -R www-data:www-data "/var/www/downloader/database"']
CMD ['chown -R www-data:www-data "/data/database"']
CMD ['chown -R www-data:www-data "/var/www/downloader/storage/app/ssh_keys"']
CMD ['chown -R www-data:www-data "/var/www/downloader/storage/logs"']
CMD ['php -r "file_exists('/data/database/database.sqlite') || touch('/data/database/database.sqlite');"']

VOLUME ["/var/www/downloader/storage/app/uploads", "/var/www/downloader/storage/app/downloads", "/var/www/downloader/storage/app/ssh_keys", "/var/www/downloader/storage/logs", "/data/database"]

CMD ["/usr/bin/supervisord"]