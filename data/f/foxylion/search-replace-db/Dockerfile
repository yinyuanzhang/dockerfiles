FROM php:7.0-apache

RUN apt-get update; apt-get install -y unzip
RUN docker-php-ext-install mysqli
RUN curl -o srdb.zip -L https://github.com/interconnectit/Search-Replace-DB/archive/3.1.zip; \
    unzip srdb.zip; \
    rm srdb.zip; \
    mv Search-Replace-DB-3.1/* .; \
    rmdir Search-Replace-DB-3.1
RUN sed -i '/$this->response();/ i\
    $name = getenv("DB_NAME") ?: NULL;\
    $user = getenv("DB_USER") ?: NULL;\
    $pass = getenv("DB_PASS") ?: NULL;\
    $host = getenv("DB_HOST") ?: "127.0.0.1";\
    $port = getenv("DB_PORT") ?: "3306";\
    $charset = getenv("DB_CHARSET") ?: "utf8";\
    $collate = getenv("DB_COLLATE") ?: "";' ./index.php
RUN sed -i "s/\$this->response();/\$this->response(\$name, \$user, \$pass, \$host, \$port, \$charset, \$collate);/g" ./index.php
