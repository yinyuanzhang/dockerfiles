FROM owasp/zap2docker-stable

MAINTAINER Chris Runo <chris.runo@mediacurrent.com>

ENV LC_ALL=C.UTF-8

USER root
CMD /bin/bash

RUN DEBIAN_FRONTEND=noninteractive apt-get -y install;

# Replace shell with bash so we can source files and install packages.
RUN rm /bin/sh && ln -s /bin/bash /bin/sh && \
    apt-get update && \
    apt-get -y upgrade; \
    apt-get -y dist-upgrade && \
    apt-get install -y software-properties-common && \
    add-apt-repository -y ppa:ondrej/php && \
    apt-get update --fix-missing;

# Install basic packages
RUN apt-get -q -y install --fix-missing \
    apache2 \
    autoconf \
    build-essential \
    bzip2 \
    ca-certificates \
    file \
    gcc \
    imagemagick \
    libc-dev \
    libfontconfig \
    libfreetype6 \
    libssl-dev \
    make \
    patch \
    pkg-config \
    rsync \
    vim ;

# Install PHP7
RUN apt-get -y install \
    libapache2-mod-php7.2 \
    php7.2 \
    php7.2-bcmath \
    php7.2-cli \
    php7.2-curl \
    php7.2-dev \
    php7.2-gd \
    php7.2-intl \
    php7.2-json \
    php7.2-mbstring \
    php7.2-mysql \
    php7.2-soap \
    php7.2-xml \
    php7.2-zip \
    php-imagick \
    php-memcache \
    php-pear;

# Install mcrypt
RUN apt-get update -y && \
    apt-get install -y libmcrypt-dev && \
    pecl install mcrypt-1.0.1;

# Enable mcrypt
RUN bash -c "echo extension= /usr/lib/php/20170718/mcrypt.so > /etc/php/7.2/cli/conf.d/mcrypt.ini" && \
    bash -c "echo extension= /usr/lib/php/20170718/mcrypt.so > /etc/php/7.2/apache2/conf.d/mcrypt.ini" && \
    service apache2 restart && \
    php -i | grep "mcrypt";


# Setup and Install MySQL server
RUN echo "mysql-server mysql-server/root_password password password" | debconf-set-selections && \
    echo "mysql-server mysql-server/root_password_again password password" | debconf-set-selections && \
    apt-get -y install mysql-server mysql-client && \
    service mysql start;
EXPOSE 3306

# Install Composer
RUN curl -sS https://getcomposer.org/installer | php -- --filename=composer --install-dir=/usr/bin;
RUN composer --verbose self-update --stable;

# Install Chromium browser and Chrome dependencies
RUN apt-get install -y \
    awscli \
    chromium-browser \
    gconf-service \
    libasound2 \
    libatk1.0-0 \
    libc6 \
    libcairo2 \
    libcups2 \
    libdbus-1-3 \
    libexpat1 \
    libfontconfig1 \
    libgcc1 \
    libgconf-2-4 \
    libgdk-pixbuf2.0-0 \
    libglib2.0-0 \
    libgtk-3-0 \
    libnspr4 \
    libpango-1.0-0 \
    libpangocairo-1.0-0 \
    libstdc++6 \
    libx11-6 \
    libx11-xcb1 \
    libxcb1 \
    libxcomposite1 \
    libxcursor1 \
    libxdamage1 \
    libxext6 \
    libxfixes3 \
    libxi6 \
    libxrandr2 \
    libxrender1 \
    libxss1 \
    libxtst6 \
    fonts-liberation \
    libappindicator1 \
    libnss3 \
    lsb-release \
    xdg-utils \
    wget;


# Install node and npm
ENV NVM_DIR /usr/local/nvm
ENV NODE_VERSION 10.12.0
RUN curl --silent -o- https://raw.githubusercontent.com/creationix/nvm/v0.31.2/install.sh | bash && \
    source $NVM_DIR/nvm.sh && \
    nvm install $NODE_VERSION && \
    nvm alias default $NODE_VERSION && \
    nvm use default;

# Add node and npm to path so the commands are available
ENV NODE_PATH $NVM_DIR/v$NODE_VERSION/lib/node_modules
ENV PATH $NVM_DIR/versions/node/v$NODE_VERSION/bin:$PATH

RUN npm config set user 0 && \
    npm config set unsafe-perm true;

# Install PhantomJS (wernight/phantomjs)
RUN mkdir /tmp/phantomjs && \
    curl -L https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2 | tar -xj --strip-components=1 -C /tmp/phantomjs && \
    mv /tmp/phantomjs/bin/phantomjs /usr/local/bin;

# Install NPM modules
RUN npm install -g pa11y@4.13.2 && \
    npm install -g lighthouse && \
    npm install -g slack-cli && \
    npm install -g forever && \
    npm install -g backstopjs;

# Clean up installs
RUN apt-get autoremove -y && \
    apt-get clean -y;
RUN rm -rf /root/.composer /tmp/*

# Link the ssh config for root for the zap user
RUN ln -sf /home/zap/.ssh /root/.ssh

CMD bash
