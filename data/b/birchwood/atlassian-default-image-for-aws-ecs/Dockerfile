FROM php:7.3
ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update && apt-get install -y jq git python-dev libyaml-dev curl zip zlib1g-dev libreadline-dev libcurl4-gnutls-dev libxml2-dev libfreetype6-dev libjpeg62-turbo-dev libpng-dev libzip-dev && \
    ln -s /usr/include/x86_64-linux-gnu/curl /usr/local/include/curl && \
    docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ && \
    docker-php-ext-install -j$(nproc) zip curl mbstring mysqli pdo_mysql gd pcntl && \
    curl -fsSL get.docker.com | bash && \
    curl -sL https://deb.nodesource.com/setup_10.x | bash - && \
    apt-get install -y nodejs libfontconfig build-essential && \
    apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
# Update npm
RUN npm install -g npm
# Composer
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer
# AWS CLI
RUN curl -sL https://bootstrap.pypa.io/get-pip.py | python && pip install awscli
# Sentry CLI
RUN curl -sL https://sentry.io/get-cli/ | bash
# ECS Deploy script
RUN curl -sS https://raw.githubusercontent.com/silinternational/ecs-deploy/3.6.0/ecs-deploy \
    | tee -a /usr/bin/ecs-deploy && chmod +x /usr/bin/ecs-deploy
# Traffic Light script
RUN curl -sS https://raw.githubusercontent.com/bluefrg/traffic-light/1.0.0/traffic-light \
    | tee -a /usr/bin/traffic-light && chmod +x /usr/bin/traffic-light
# Auto Merge script
RUN curl -sS https://raw.githubusercontent.com/bluefrg/bitbucket-auto-merge/1.0.0/bitbucket-auto-merge \
    | tee -a /usr/bin/bitbucket-auto-merge && chmod +x /usr/bin/bitbucket-auto-merge
