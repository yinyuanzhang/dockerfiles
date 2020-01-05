FROM ubuntu:yakkety

MAINTAINER chukin <admin@kusumpharm.com>

ENV php_conf /etc/php/7.0/fpm/php.ini
ENV fpm_conf /etc/php/7.0/fpm/php-fpm.conf
ENV fpm_pool_conf /etc/php/7.0/fpm/pool.d/www.conf
ENV php_cli_conf /etc/php/7.0/cli/php.ini

RUN apt-get update && \
    apt-get install --no-install-recommends --no-install-suggests -y \
    ca-certificates \
	nginx \
	gettext-base \
	apt-transport-https \
    bash \
    software-properties-common \
    openssh-client \
    wget \
    supervisor \
    curl \
    git \
    cron \
    libxml2-dev \
    php-fpm \
    php-mcrypt \
    php-common \
    php-gd \
    php-intl \
    php-memcache \
    php-xsl \
    php-curl \
    php-json \
    php-gearman \
    php-apcu \
    php-sybase \
    php-xml \
    php-pear \
    php-dev \
    php7.0-mbstring \
    php-zip \
    gnupg2 \
    gcc \
    musl-dev \
    gearman-job-server \
    libgearman-dev \
    gcc \
    g++ \
    nano \
    rsync \
    build-essential \
    libffi-dev &&\
    mkdir -p /etc/nginx && \
    mkdir -p /run/nginx && \
    mkdir -p /var/log/supervisor &&\
    mkdir -p /run/php &&\
    php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');" && \
    php composer-setup.php --install-dir=/usr/bin --filename=composer && \
    php -r "unlink('composer-setup.php');"

RUN curl -sL https://deb.nodesource.com/setup_7.x | bash -
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
RUN	curl https://packages.microsoft.com/config/ubuntu/16.10/prod.list > /etc/apt/sources.list.d/mssql-release.list
RUN curl -L https://packages.gitlab.com/install/repositories/runner/gitlab-ci-multi-runner/script.deb.sh | bash
RUN apt-get update
RUN	ACCEPT_EULA=Y apt-get install -y msodbcsql
RUN	apt-get install -y unixodbc-dev nodejs gitlab-ci-multi-runner
RUN	pecl install sqlsrv pdo_sqlsrv
RUN echo "extension= pdo_sqlsrv.so" >> ${php_conf} && \
	echo "extension= sqlsrv.so" >> ${php_conf} && \
	echo "extension= pdo_sqlsrv.so" >> ${php_cli_conf} && \
    echo "extension= sqlsrv.so" >> ${php_cli_conf}
RUN localedef -i en_US -f UTF-8 en_US.UTF-8

ADD conf/supervisord.conf /etc/supervisord.conf
# Cron config clear
RUN rm -Rf /etc/cron.d/*
# Copy our nginx config
RUN rm -Rf /etc/nginx/nginx.conf
ADD conf/nginx.conf /etc/nginx/nginx.conf

# nginx site conf
RUN mkdir -p /etc/nginx/sites-available/ && \
mkdir -p /etc/nginx/sites-enabled/ && \
mkdir -p /etc/nginx/ssl/ && \
mkdir -p /var/www/html/

# forward request and error logs to docker log collector
RUN ln -sf /dev/stdout /var/log/nginx/access.log \
	&& ln -sf /dev/stderr /var/log/nginx/error.log

RUN rm -Rf /etc/nginx/sites-enabled/*

ADD conf/nginx-site.conf /etc/nginx/sites-available/default.conf
RUN ln -s /etc/nginx/sites-available/default.conf /etc/nginx/sites-enabled/default.conf

# tweak php-fpm config
RUN sed -i \
        -e "s/;cgi.fix_pathinfo=1/cgi.fix_pathinfo=0/g" \
        -e "s/upload_max_filesize\s*=\s*2M/upload_max_filesize = 100M/g" \
        -e "s/post_max_size\s*=\s*8M/post_max_size = 100M/g" \
        -e "s/variables_order = \"GPCS\"/variables_order = \"EGPCS\"/g" \
        -e "s/;date.timezone =/date.timezone = \"Europe\/Kiev\"/g" \
        ${php_conf} && \
    sed -i \
        -e "s/;daemonize\s*=\s*yes/daemonize = no/g" \
        ${fpm_conf} && \
    sed -i \
        -e "s/;catch_workers_output\s*=\s*yes/catch_workers_output = yes/g" \
        -e "s/pm.max_children = 4/pm.max_children = 4/g" \
        -e "s/pm.start_servers = 2/pm.start_servers = 3/g" \
        -e "s/pm.min_spare_servers = 1/pm.min_spare_servers = 2/g" \
        -e "s/pm.max_spare_servers = 3/pm.max_spare_servers = 4/g" \
        -e "s/pm.max_requests = 500/pm.max_requests = 200/g" \
        -e "s/;listen.mode = 0660/listen.mode = 0666/g" \
        -e "s/^;clear_env = no$/clear_env = no/" \
        -e "s/;realpath_cache_size = 16k/realpath_cache_size = 4096k/g" \
        ${fpm_pool_conf} && \
    ln -s /etc/php/7.0/fpm/php.ini /etc/php/7.0/fpm/conf.d/php.ini && \
    find /etc/php/7.0/fpm/conf.d/ -name "*.ini" -exec sed -i -re 's/^(\s*)#(.*)/\1;\2/g' {} \;

RUN npm install -g bower gulp

# Add Scripts
ADD scripts/start.sh /start.sh
ADD scripts/php-watcher.sh /usr/bin/php-watcher.sh
ADD scripts/enable_xdebug.sh /enable_xdebug.sh
RUN chmod 755 /start.sh && chmod 755 /usr/bin/php-watcher.sh && chmod 755 /enable_xdebug.sh

VOLUME /var/www/html

EXPOSE 80

#CMD ["/usr/bin/supervisord", "-n", "-c",  "/etc/supervisord.conf"]
CMD ["/start.sh"]
