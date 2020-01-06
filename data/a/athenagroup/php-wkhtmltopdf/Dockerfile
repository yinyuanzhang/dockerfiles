FROM webdevops/php-apache:7.2

# Environment variables
ENV WEB_DOCUMENT_ROOT=/app/public

# Commont tools
RUN apt-get update && apt-get dist-upgrade -y && apt-get install -y \
    sudo \
    libfreetype6-dev \
    mysql-client \
    build-essential \
    libxrender1 \
    libfontconfig1 \
    libssl1.0-dev \
    nano

# Install wkhtmltopdf
RUN cd /tmp && wget https://github.com/wkhtmltopdf/wkhtmltopdf/releases/download/0.12.4/wkhtmltox-0.12.4_linux-generic-amd64.tar.xz && \
    tar -xvf wkhtmltox-0.12.4_linux-generic-amd64.tar.xz && \
    mv -v wkhtmltox/bin/* /usr/local/bin/

# Reconfigure GD
RUN docker-php-ext-configure gd \
    --with-gd \
    --with-freetype-dir=/usr/include/ \
    --with-png-dir=/usr/include/ \
    --with-jpeg-dir=/usr/include/

# Add application user to sudoers
RUN usermod -aG sudo ${APPLICATION_USER} \
    && echo "${APPLICATION_USER} ALL=(ALL:ALL) NOPASSWD: ALL" >> /etc/sudoers.d/${APPLICATION_USER}

# Finalize installation and clean up
RUN docker-service enable postfix \
    && docker-run-bootstrap \
    && docker-image-cleanup \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Imap uninstall workaround
RUN rm /usr/local/etc/php/conf.d/docker-php-ext-imap.ini    

# Change user
USER ${APPLICATION_USER}

# Composer parallel install plugin
RUN composer global require hirak/prestissimo

# Container must start as root user
USER root

# Default work dir
WORKDIR ${APPLICATION_PATH}
