FROM eirwego/heavy-eir-api

COPY --from=composer /usr/bin/composer /usr/bin/composer

RUN curl https://cli-assets.heroku.com/install.sh | sh \
 && apt-get install -y gnupg \
 && curl https://deb.nodesource.com/setup_12.x | bash \
 && apt-get install -y git libzip-dev nodejs unzip zlib1g-dev \
 && apt-get clean \
 && docker-php-ext-install -j$(nproc) zip \
 && /ppm/vendor/bin/ppm config --app-env=dev --config=/ppm/ppm.json --debug=1 \
 && npm install --allow-root --global --unsafe-perm=true dredd
