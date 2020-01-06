FROM debian:jessie
MAINTAINER Geoffrey Tran <geoffrey.tran@gmail.com>

# Disable user prompts
ENV DEBIAN_FRONTEND noninteractive

# App install directory
ENV PROJECT_DIR /srv

# Set node environment to production to prevent installing dev dependencies
ENV NODE_ENV production

# Update the repository sources list
RUN \
    apt-get update -q && \
    apt-get install --no-install-recommends -qy wget ca-certificates python-setuptools \
        supervisor sendmail-bin htop curl nano git mysql-client netcat redis-tools \
        php5-fpm php5-cli php5-curl php5-gd php5-json php5-ldap php5-mysql \
        php5-odbc php5-pgsql php5-pspell php5-readline php5-sqlite php5-tidy \
        php5-xmlrpc php5-xsl php5-intl php5-apcu php5-mcrypt php5-memcache \
        php5-memcached php5-redis php5-mongo php5-twig php5-xdebug phpunit && \

    apt-get install --no-install-recommends -qy cron && \

    apt-get install --no-install-recommends -qy nginx && \
    echo "\ndaemon off;" >> /etc/nginx/nginx.conf && \
    chown -R www-data:www-data /var/lib/nginx && \

    sh -c 'echo deb http://apt.newrelic.com/debian/ newrelic non-free >> /etc/apt/sources.list.d/newrelic.list' && \
    wget -O- https://download.newrelic.com/548C16BF.gpg | apt-key add - && \
    apt-get update -q && \
    apt-get install --no-install-recommends -qy newrelic-php5  && \

    apt-get install --no-install-recommends -qy nodejs npm && \
    npm install --loglevel warn -g less && \
    npm install --loglevel warn -g uglify-js && \
    npm install --loglevel warn -g uglifycss && \
    npm install --loglevel warn -g autoprefixer@5.2 && \
    npm install --loglevel warn -g bower && \
    ln -s /usr/local/bin/autoprefixer /usr/bin/autoprefixer && \
    ln -s /usr/local/bin/uglifycss /usr/bin/uglifycss && \
    ln -s /usr/local/bin/uglifyjs /usr/bin/uglifyjs && \
    ln -s /usr/bin/nodejs /usr/bin/node && \

    apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Install composer
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer

# Copy cron files
COPY var/docker/cron/cron.d/ /etc/cron.d/

# Copy php.ini
COPY var/docker/php.ini /etc/php5/cli/php.ini
COPY var/docker/php.ini /etc/php5/fpm/php.ini

# Copy php5 modules config
COPY var/docker/php5/mods-available/newrelic.ini.dist /etc/php5/mods-available/newrelic.ini.dist

# Copy php-fpm
COPY var/docker/php-fpm.conf /etc/php5/fpm/php-fpm.conf

# Copy nginx config
COPY var/docker/nginx/nginx.conf /etc/nginx/nginx.conf
COPY var/docker/nginx/conf.d/default.conf.dist /etc/nginx/conf.d/default.conf.dist
COPY var/docker/nginx/html /usr/share/nginx/html

# Copy supervisor config
COPY var/docker/supervisor/conf.d /etc/supervisor/conf.d/

COPY . ${PROJECT_DIR}

WORKDIR ${PROJECT_DIR}

# Set assets version
RUN GITHASH=`git rev-parse --short HEAD` sh -c  'sed -i "s/assets.version\(.*\)=\(.*\)/assets.version\1= $GITHASH/" config/parameters.ini.dist'

# Install dependencies and remove .git folders
RUN composer install -o --no-interaction --prefer-dist \
    && find . -type d -name .git -exec rm -rf {} +

# Install assets
RUN php app/console assets:install --env=prod --no-debug && php app/console assetic:dump --env=prod --no-debug

# Clear app caches and logs
RUN rm -fr var/cache/* && rm -fr var/log/*

# Forward Nginx request and error logs to docker log collector
RUN ln -sf /dev/stdout /var/log/nginx/access.log \
    && ln -sf /dev/stderr /var/log/nginx/error.log \
    && rm -fr /etc/nginx/sites-enabled/default

EXPOSE 9000 80 443

VOLUME ${PROJECT_DIR}

# Copy entrypoint
COPY var/docker/entrypoint.sh /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]

# Run cron
#CMD ["cron", "-f"]

# Run php5-fpm
#CMD ["php5-fpm", "-F"]

# Run nginx
#CMD ["nginx"]

# Run supervisord which should run the basic services we need (nginx/php5-fpm) locally
CMD ["supervisord"]
