FROM php:7.0-stretch

# --------------------------------
# Update OS
# --------------------------------
RUN apt-get -y update && apt-get -y upgrade

# --------------------------------
# Install key packages
# --------------------------------
RUN apt-get install -y \
    python-pip \
    git \
    subversion \
    openssh-server \
    mercurial \
    bash \
    curl \
    wget \
    zip \
    patch \
    zlib1g-dev \
    libpng-dev \
    apt-transport-https \
    gnupg

# --------------------------------
# Config memory limit and timezone
# --------------------------------
RUN echo "memory_limit=-1" > "$PHP_INI_DIR/conf.d/memory-limit.ini" \
    && echo "date.timezone=${PHP_TIMEZONE:-UTC}" > "$PHP_INI_DIR/conf.d/date_timezone.ini"

# --------------------------------
# Install PHP extensions
# --------------------------------
RUN docker-php-ext-install zip pdo_mysql gd

# --------------------------------
# Set composer envs
# --------------------------------
ENV COMPOSER_ALLOW_SUPERUSER 1
ENV COMPOSER_VERSION 1.7.1

# --------------------------------
# Download and install composer
# --------------------------------
RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');"
RUN php -r "if (hash_file('sha384', 'composer-setup.php') === '48e3236262b34d30969dca3c37281b3b4bbe3221bda826ac6a9a62d6444cdb0dcd0615698a5cbe587c3f0fe57a54d8f5') { echo 'Installer verified'; } else { echo 'Installer corrupt'; unlink('composer-setup.php'); } echo PHP_EOL;"
RUN php composer-setup.php --no-ansi --install-dir=/usr/bin --filename=composer --version=${COMPOSER_VERSION} \
    && composer --ansi --version --no-interaction \
    && rm -rf /tmp/* /tmp/.htaccess
RUN php -r "unlink('composer-setup.php');"

# --------------------------------
# Download and install heroku cli
# --------------------------------
RUN curl https://cli-assets.heroku.com/install-ubuntu.sh | sh

# --------------------------------
# Download and install AWS Elastic Beanstalk cli
# --------------------------------
RUN pip install awsebcli --upgrade
RUN eb --version

# --------------------------------
# Set working directory
# --------------------------------
WORKDIR /app
