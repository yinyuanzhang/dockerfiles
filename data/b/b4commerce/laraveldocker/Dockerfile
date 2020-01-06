FROM php:7.2-apache-stretch

COPY --from=composer /usr/bin/composer /usr/bin/composer

# Install modules
RUN apt-get update && apt-get install -y \
    git \
    libssl-dev \
    libfreetype6-dev \
    libjpeg62-turbo-dev \
    libmcrypt-dev \
    libpng-dev \
	libxml2-dev \
	libpq-dev \
	software-properties-common \
	gnupg \
	zip \
	unzip \
	libbz2-dev \
	libfontconfig
RUN docker-php-ext-install mbstring tokenizer pcntl pdo pdo_mysql pdo_pgsql bcmath \
    && docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ \
    && docker-php-ext-install gd zip ctype json soap intl bz2


# Install node
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash - && \
    apt-get install -y nodejs && \
    apt-get install -y build-essential

# Install puppeteer
RUN apt-get install -y gconf-service libasound2 libatk1.0-0 libc6 libcairo2 libcups2 libdbus-1-3 libexpat1 libfontconfig1 libgcc1 libgconf-2-4 libgdk-pixbuf2.0-0 libglib2.0-0 libgtk-3-0 libnspr4 libpango-1.0-0 libpangocairo-1.0-0 libstdc++6 libx11-6 libx11-xcb1 libxcb1 libxcomposite1 libxcursor1 libxdamage1 libxext6 libxfixes3 libxi6 libxrandr2 libxrender1 libxss1 libxtst6 ca-certificates fonts-liberation libappindicator1 libnss3 lsb-release xdg-utils wget && \
    npm install --global --unsafe-perm puppeteer && \
    chmod -R o+rx /usr/lib/node_modules/puppeteer/.local-chromium && \
    rm -rf /var/lib/apt/lists/* && \
    apt-get clean

COPY . /var/www/html
COPY ./vhost.conf /etc/apache2/sites-available/000-default.conf
COPY ./start.sh /usr/local/bin/start

RUN chown -R www-data:www-data /var/www/html \
    && chmod u+x /usr/local/bin/start \
    && a2enmod rewrite headers

CMD ["/usr/local/bin/start"]
