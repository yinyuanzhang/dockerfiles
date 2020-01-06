FROM  php:7.0-fpm 

RUN apt-get update && apt-get install -y \
  libicu-dev \
  libpq-dev \
  zip \
  unzip \
  # https://github.com/Safran/RoPA/issues/4
  libzip-dev \
  # https://stackoverflow.com/questions/2977662/php-zip-installation-on-linux
  zlib1g-dev \
  && rm -r /var/lib/apt/lists/*
# configure the php modules
RUN docker-php-ext-configure pdo_mysql --with-pdo-mysql=mysqlnd \
  && docker-php-ext-install \
  intl \
  mbstring \
  pcntl \
  pdo_mysql \
  zip \
  opcache
  
RUN groupadd -g 999 appuser && \
    useradd -r -u 999 -g appuser appuser
USER appuser