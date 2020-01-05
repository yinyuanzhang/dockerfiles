FROM profideo/php-7.1.6-fpm

# Install Composer
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer

# Install PHP extensions
RUN apt-get update && apt-get install -y zlib1g-dev
RUN docker-php-ext-install pdo pdo_mysql zip sockets

# Install ClamAV
RUN apt-get update && apt-get install -y clamav clamav-freshclam clamav-daemon

# Install nodejs
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash -
RUN apt-get update && apt-get install -y nodejs
# @see http://symfony.com/doc/current/frontend/encore/installation.html

# Install yarn for symfony/webpack-encore
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -
RUN echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list
RUN apt-get update && apt-get install yarn
#RUN npm install -g @symfony/webpack-encore --save-dev
#RUN npm install -g node-sass

# Nginx configuration
COPY files/nginx.conf /etc/nginx/nginx.conf

# Supervisor
COPY files/supervisord.conf /etc/supervisor/conf.d/supervisord.conf
CMD ["/usr/bin/supervisord"]
