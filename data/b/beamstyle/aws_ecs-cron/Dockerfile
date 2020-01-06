FROM php:7.0-cli

MAINTAINER Thomas Cheng <thomas@beamstyle.com.hk>

# Reference DockerFile: https://github.com/meanbee/docker-magento2

# Install dependencies
RUN \
    apt-get update && apt-get install -y      \
        libicu-dev                            \ 
        libmcrypt-dev                         \ 
        libxslt1-dev                          \ 
        sudo                                  \ 
        cron                                  \ 
        rsyslog                               \ 
        mysql-client                          \ 
        git                                   \
        libzip-dev                            \
        zlib1g-dev                            \
                                              \
        `# GD library`                        \
        libfreetype6-dev                      \
        libjpeg62-turbo-dev                   \
        libpng-dev                            \
        libwebp-dev                           \
                                              \
    `# Remove unwanted files`                 \
    && rm -rf /var/lib/apt/lists/*
    
# Configure required PHP extensions
RUN \
    docker-php-ext-install                    \
        dom                                   \ 
        intl                                  \ 
        mbstring                              \ 
        pdo_mysql                             \ 
        xsl                                   \ 
        zip                                   \ 
        soap                                  \ 
        bcmath                                \ 
        mcrypt

# Configure GD library
RUN \
    docker-php-ext-configure gd               \
        --with-freetype-dir=/usr/include/     \
        --with-jpeg-dir=/usr/include/         \
        --with-png-dir=/usr/include/          \
        --with-webp-dir=/usr/include/         \
                                              \
    && docker-php-ext-install gd

ENV SRC_ROOT /var/www/html

ADD run.sh /usr/local/bin/

RUN ["chmod", "+x", "/usr/local/bin/run.sh"]

CMD ["/usr/local/bin/run.sh"]
