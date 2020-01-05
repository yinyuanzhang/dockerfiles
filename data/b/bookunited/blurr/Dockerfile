FROM debian:9

ARG development="0"

RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-selections

RUN apt-get update -q \
    && apt-get install -yq \
       unzip \
       locales \
       nginx \
       supervisor \
       curl \
       wget \
       git \
       apt-transport-https \
       lsb-release \
       ca-certificates \
       jq \
       python-pip \
       groff \
    && wget -O /etc/apt/trusted.gpg.d/php.gpg https://packages.sury.org/php/apt.gpg \
    && echo "deb https://packages.sury.org/php/ $(lsb_release -sc) main" | tee /etc/apt/sources.list.d/php.list \
    && apt-get update -q \
    && apt-get install -yq \
        php7.2-fpm \
        php7.2-cli \
        php7.2-common \
        php7.2-mbstring \
        php7.2-mysql \
        php7.2-sqlite \
        php7.2-xml \
        php7.2-curl \
        php7.2-soap \
        php7.2-gd \
    && pip install awscli \
    && curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/bin --filename=composer \
    && mkdir -p /run/php \
    && ln -sf /dev/stdout /var/log/nginx/access.log \
    && ln -sf /dev/stderr /var/log/nginx/error.log \
    && apt-get -y autoremove \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \
    && ln -sf /dev/stdout /var/log/nginx/access.log \
    && ln -sf /dev/stderr /var/log/nginx/error.log

COPY certs/localhost.crt certs/localhost.key /etc/nginx/
COPY default /etc/nginx/sites-available/default
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf
COPY locale.gen /etc/locale.gen

RUN locale-gen

# Install development packages
RUN if [ "$development" = "1" ]; \
then \
    version=$(php -r "echo PHP_MAJOR_VERSION.PHP_MINOR_VERSION;") \
    && curl -A "Docker" -o /tmp/blackfire-probe.tar.gz -D - -L -s https://blackfire.io/api/v1/releases/probe/php/linux/amd64/$version \
    && mkdir -p /tmp/blackfire \
    && tar zxpf /tmp/blackfire-probe.tar.gz -C /tmp/blackfire \
    && mv /tmp/blackfire/blackfire-*.so $(php -r "echo ini_get('extension_dir');")/blackfire.so \
    && printf "extension=blackfire.so\nblackfire.agent_socket=tcp://blackfire:8707\n" > /etc/php/7.2/fpm/conf.d/blackfire.ini \
    && rm -rf /tmp/blackfire /tmp/blackfire-probe.tar.gz \
    && apt-get update -q \
    && apt-get install php7.2-xdebug \
    && apt-get -y autoremove \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*; \
fi

WORKDIR /var/www/html

EXPOSE 80 443

CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]