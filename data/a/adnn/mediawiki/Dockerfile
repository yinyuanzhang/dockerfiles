FROM mediawiki:1.32


## We do not use Math extension anymore
## because it dropped support for MathJax
#RUN git clone --depth 1 -b $MEDIAWIKI_BRANCH \
#    https://gerrit.wikimedia.org/r/p/mediawiki/extensions/Math \
#    /var/www/html/extensions/Math


## Use SimpleMathJax
## atm: my fork, adding "autoload-all" MathJax extension
RUN git clone --depth 1 https://github.com/Adnn/SimpleMathJax.git \ 
    /var/www/html/extensions/SimpleMathJax


## SemanticMediaWiki extension
COPY composer.local.json .

RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');" \
    && php -r "if (hash_file('sha384', 'composer-setup.php') === '48e3236262b34d30969dca3c37281b3b4bbe3221bda826ac6a9a62d6444cdb0dcd0615698a5cbe587c3f0fe57a54d8f5') { echo 'Installer verified'; } else { echo 'Installer corrupt'; unlink('composer-setup.php'); } echo PHP_EOL;" \
    && php composer-setup.php \
    && php -r "unlink('composer-setup.php');" \
    && apt-get update \
    && apt-get install -y unzip mysql-client \
    && php composer.phar update --no-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*


## Clone the backup project
RUN git clone --depth 1 https://github.com/Adnn/MediaWiki_Backup.git


## Install the logic to run custom entrypoint scripts
RUN git clone -c advice.detachedHead=false --depth 1 --branch 1.0.0 https://github.com/Adnn/docker-entrypoint.git \
    && mv docker-entrypoint/docker-entrypoint.sh / \
    && rm -r docker-entrypoint/


# Forwarding to original entrypoint, found in PHP image
# see: https://github.com/docker-library/php/blob/d9352e08aa39f699cfedb2b564aeb60955b06469/7.2/stretch/apache/Dockerfile#L282-L288
# note that overriding ENTRYPOINT also null CMD
# see: https://stackoverflow.com/a/49031590/1027706
ENTRYPOINT ["/docker-entrypoint.sh", "docker-php-entrypoint"]
CMD ["apache2-foreground"]
