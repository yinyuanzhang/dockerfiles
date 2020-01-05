FROM ubuntu:16.10

RUN apt-get update && apt-get install -y curl \
    && curl -sL https://deb.nodesource.com/setup_7.x | bash \
    && apt install -y nodejs \
    && npm install pm2@2.1.6 -g \
    && npm install less -g \
    && npm install less-plugin-clean-css -g \
    && npm install npm@4.0.3 -g \
    && apt-get autoclean \
    && mkdir /var/www \
    && chown www-data: /var/www

WORKDIR /app

CMD ["bash", "-c", "pm2-docker --raw --env production $SITE_ROOT/ecosystem.config.js"]
