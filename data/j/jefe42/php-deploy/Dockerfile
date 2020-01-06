FROM debian:sid-slim

RUN apt-get update -q && apt-get install -qqy \
    # Need to install procps so that we get the 'ps' command.
    procps \
    git-core \
    composer \
    # Installing Apache and PHP-FPM
    php7.2 \
    php-intl \
    php-mbstring \
    php-zip \
    php-xml \
    php-curl \
    php-soap \
    php-bcmath \
    php-gmp \
    php-codesniffer && \
    # Purge the apt list software to save space.
    rm -rf /var/lib/apt/lists/*

