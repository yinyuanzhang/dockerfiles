FROM php:7.2-cli

RUN apt-get clean && apt-get update && apt-get install -y locales

# Among other things, ensure that UTF characters in a PPA name don't break things.
RUN locale-gen en_US.UTF-8
ENV LANG en_US.UTF-8

# Install packages.
RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get -qq -o Dpkg::Options::="--force-confold" install \
    git \
    rsync \
    ssh \
    ruby \
    wget \
    gnupg \
    zip \
    zlib1g-dev \
    && apt-get clean && rm -rf /tmp/* /var/lib/apt/lists/* /var/tmp/*
	
# Set some PHP config data.
RUN echo "date.timezone = America/New_York;" > /usr/local/etc/php/conf.d/general.ini
RUN echo "memory_limit = 512M;" >> /usr/local/etc/php/conf.d/general.ini

# install the PHP extensions we need
RUN docker-php-ext-install -j "$(nproc)" \
		zip \
	;

# Install Composer.
RUN curl --silent --output /tmp/composer-setup.php https://getcomposer.org/installer && \
    php /tmp/composer-setup.php --install-dir=/usr/local/bin --filename=composer --version=1.7.3 && \
    rm /tmp/composer-setup.php


# Install LTS release of nodejs 6.x from nodesource. This is based off instructions from
# https://nodejs.org/en/download/package-manager/#debian-and-ubuntu-based-linux-distributions
RUN ["/bin/bash", "-c", "set -o pipefail && curl -sL https://deb.nodesource.com/setup_8.x | bash -"]
RUN apt-get install -y nodejs
# It will install to executable "nodejs" but we want to run it by using just "node", so symlink
# to that path.
RUN ln -s `which nodejs` /usr/local/bin/node
# Update NPM
RUN npm install -g npm@6.4.1

# Disable strict host key checking. Acquia provisioning the SVN server
# without notice, so we don't know when to update host keys.
RUN mkdir /root/.ssh
RUN printf "\nHost *\n    StrictHostKeyChecking no" >> ~/.ssh/config

