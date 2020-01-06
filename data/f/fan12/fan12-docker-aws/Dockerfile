
FROM docker:git

# Install Python, AWS CLI and EB CLI
RUN apk add --no-cache curl jq python3 py-pip
RUN pip install awscli
RUN pip install awsebcli

# Install PHP and Composer
RUN apk --update add wget curl git php php-curl php-openssl php-json php-phar php-dom php-iconv php-mbstring php-simplexml php-gd freetype-dev libpng-dev libjpeg-turbo-dev && rm /var/cache/apk/*
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/bin --filename=composer 
