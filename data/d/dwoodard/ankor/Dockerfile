FROM php:7.1-apache

MAINTAINER Dustin Woodard <dustin.woodard@gmail.com>

#  Installs Utils and Apache

RUN mkdir -p /var/www
RUN usermod -u 1000 www-data
RUN usermod -a -G users www-data
RUN chown -R www-data:www-data /var/www/

RUN apt-get -qq update && apt-get install -y \
 git-core \
 vim \
 unzip \
 curl \
 wget \
 && apt-get clean
#software-properties-common \




# Setting document root
RUN mkdir /var/www/html/public/
RUN sed -i "s#.*DocumentRoot /var/www/html#\tDocumentRoot /var/www/html/public#" /etc/apache2/sites-enabled/000-default.conf
RUN sed -i "s#\#ServerName www.example.com#ServerName localhost#" /etc/apache2/sites-enabled/000-default.conf
RUN sed -i 's/AllowOverride None/AllowOverride All/' /etc/apache2/apache2.conf

RUN service apache2 restart
RUN a2enmod rewrite

# Correct Time
RUN echo "America/Denver" | tee /etc/timezone
RUN dpkg-reconfigure --frontend noninteractive tzdata

RUN mkdir -p /etc/ssl/server/certs

# Make CERT
RUN openssl req -new -newkey rsa:4096 -days 3652 -nodes -x509 -subj "/C=US/ST=UT/L=Ogden/O=IT/CN=docker.dev" -keyout /etc/ssl/server/certs/server.pem  -out /etc/ssl/server/certs/server.cert

ADD app.conf /etc/apache2/sites-available/

RUN a2ensite app.conf
RUN a2enmod ssl


RUN docker-php-source extract \
&& apt-get update \
&& apt-get install vim -y \
&& docker-php-ext-install mysqli pdo pdo_mysql \
&& a2enmod rewrite \
&& a2enmod ssl \
&& docker-php-source delete


RUN apt-get install -y wget && \
    wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub |  apt-key add - && \
    sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list' && \
    apt-get update && apt-get install -y google-chrome-stable && \
    apt-get install -y xvfb


# Composer is the future. But you knew that did you Nice job.
RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');"
RUN php composer-setup.php --install-dir=/usr/local/bin --filename=composer
RUN php -r "unlink('composer-setup.php');"

RUN apt-get update
RUN apt-get install build-essential libssl-dev -y

#Node
RUN curl -sL https://deb.nodesource.com/setup_7.x | bash -

RUN apt-get install nodejs -y
RUN apt-get install build-essential

RUN npm -v
RUN node -v

#sqllite
RUN apt-get install sqlite3 libsqlite3-dev -y

# ChromeDriver
RUN wget https://chromedriver.storage.googleapis.com/2.33/chromedriver_linux64.zip \
&& unzip chromedriver_linux64.zip \
&& mv chromedriver /usr/bin/chromedriver \
&& rm chromedriver_linux64.zip \
&& chromedriver -v

#ImageMagick
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        libmagickwand-dev \
    && rm -rf /var/lib/apt/lists/*

RUN pecl install imagick-3.4.3 \
    && docker-php-ext-enable imagick



EXPOSE 80
EXPOSE 443

CMD /usr/sbin/apache2ctl -D FOREGROUND
