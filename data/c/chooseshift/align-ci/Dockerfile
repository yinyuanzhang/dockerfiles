
# ==============================================================================
# Shift Circle CI build image
# ==============================================================================

FROM circleci/php:7.1-stretch-node-browsers

# ==============================================================================
# Install Required Packages
# ==============================================================================

# Install required packages
RUN sudo apt update && \
    sudo apt install zlib1g-dev libsqlite3-dev libmcrypt-dev git \
                     unzip wget libpng-dev libsqlite3-dev libnss3 libgconf-2-4 \
                     libfontconfig1 chromium=73.0.3683.75-1~deb9u1 xvfb

# ==============================================================================
# PHP Extensions
# ==============================================================================

RUN sudo docker-php-ext-install zip pdo pdo_mysql bcmath

# ==============================================================================
# PHP Config
# ==============================================================================

# Use the default production / devel configuration
# RUN mv "$PHP_INI_DIR/php.ini-production" "$PHP_INI_DIR/php.ini"
RUN sudo mv "$PHP_INI_DIR/php.ini-development" "$PHP_INI_DIR/php.ini"

# Replace and copy our config files into image
COPY ./*.ini $PHP_INI_DIR/conf.d/
