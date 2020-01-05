FROM node:10-stretch
ARG DEBIAN_FRONTEND=noninteractive

# python aws
RUN set -ex; \
    apt-get update; \
    apt-get install -y --no-install-recommends \
        ca-certificates \
        apt-transport-https \
        apt-utils \
        python \
        python-dev \
        python-pip \
        python-setuptools; \
        rm -rf /var/lib/apt/lists/*; \
        pip install wheel; \
        pip install awscli

# php-cli      
ENV APT_KEY_DONT_WARN_ON_DANGEROUS_USAGE 1
RUN wget -q https://packages.sury.org/php/apt.gpg -O- | apt-key add -; \
    echo "deb https://packages.sury.org/php/ stretch main" | tee /etc/apt/sources.list.d/php.list; \
    apt-get update; \
    apt-get install -y --no-install-recommends \
        zip \
        php7.2-bcmath \
        php7.2-cli \
        php7.2-common \
        php7.2-curl \
        php7.2-gd \
        php7.2-json \
        php7.2-mbstring \
        php7.2-mysql \
        php7.2-zip \
        php7.2-intl \
        php7.2-xml; \
    rm -rf /var/lib/apt/lists/*

# cairo     
RUN apt-get update; \
    apt-get install -y --no-install-recommends \
        libcairo2 \
        libcairo2-dev; \
    rm -rf /var/lib/apt/lists/*    
