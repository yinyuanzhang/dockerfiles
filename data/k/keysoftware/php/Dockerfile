# Debian: PHP 7.0 - Build Tools
#
# - ApiGen
# - Phing
# - PHP Coding Standards Fixer (php-cs-fixer)
# - PHP Copy/Paste Detector (phpcpd)
# - PHP Depend (pdepend)
# - PHP Mess Detector (phpmd)
# - PHP Lines of Code (phploc)
# - PHP_CodeSniffer (phpcs)
# - phpDocumentor (phpdoc)
# - PhpMetrics (phpmetrics)
# - PHPUnit

# Pull the base image.
FROM debian:jessie

# Set UID.
USER root

# Set environment variables.
ENV APP_DIR         /srv/www/webapp
ENV BUILD_DIR       ${APP_DIR}/build
ENV BUILDXML        /config/build.xml
ENV COMPOSER_HOME   $HOME/.composer
ENV GITHUB_TOKEN    4d4a63415908c89118216dd2e5254fa4101796ba
ENV HOME            /home/root
ENV PATH            vendor/bin:$COMPOSER_HOME/vendor/bin:$PATH
ENV PHP_VERSION     7.0
ENV PHPUNIT_VERSION 5.0.*

# Install build dependencies.
RUN apt-get update && apt-get install -y curl git wget

# Install PHP.
RUN echo "deb http://packages.dotdeb.org jessie all" >> /etc/apt/sources.list; \
    wget https://www.dotdeb.org/dotdeb.gpg; \
    apt-key add dotdeb.gpg; \
    apt-get update && apt-get install -y \
    php${PHP_VERSION}-apcu \
    php${PHP_VERSION}-common \
    php${PHP_VERSION}-curl \
    php${PHP_VERSION}-cli \
    php${PHP_VERSION}-mysql \
    php${PHP_VERSION}-opcache \
    php${PHP_VERSION}-bz2 \
    php${PHP_VERSION}-xdebug \
    php${PHP_VERSION}-xsl

# Install Composer.
RUN mkdir -p $COMPOSER_HOME/vendor/bin; \
	curl -sS https://getcomposer.org/installer | php -- --install-dir=$COMPOSER_HOME/vendor/bin --filename=composer; \
    composer --version; \
    composer config --global github-oauth.github.com $GITHUB_TOKEN

# Install PHPUnit.
RUN composer self-update; \
    composer global require "phpunit/phpunit=${PHPUNIT_VERSION}"; \
    composer global update

# Install phpDocumentor.
RUN composer self-update; \
	composer global require "phpdocumentor/phpdocumentor=2.*"; \
	composer global update

# Install PhpMetrics.
RUN wget https://github.com/Halleck45/PhpMetrics/raw/master/build/phpmetrics.phar; \
	chmod +x phpmetrics.phar; \
	mv phpmetrics.phar /usr/local/bin/phpmetrics

# Install PHP_CodeSniffer.
RUN composer self-update; \
	composer global require "squizlabs/php_codesniffer"; \
	composer global update

# Install PHP Depend.
RUN wget http://static.pdepend.org/php/latest/pdepend.phar; \
	chmod +x pdepend.phar; \
	mv pdepend.phar /usr/local/bin/pdepend

# Install PHP Mess Detector.
RUN wget http://static.phpmd.org/php/latest/phpmd.phar; \
	chmod +x phpmd.phar; \
	mv phpmd.phar /usr/local/bin/phpmd

# Install PHP Lines of Code.
RUN wget https://phar.phpunit.de/phploc.phar; \
	chmod +x phploc.phar; \
	mv phploc.phar /usr/local/bin/phploc

# Install PHP Copy/Paste Detector.
RUN wget https://phar.phpunit.de/phpcpd.phar; \
	chmod +x phpcpd.phar; \
	mv phpcpd.phar /usr/local/bin/phpcpd

# Install PHP Coding Standards Fixer.
RUN wget http://get.sensiolabs.org/php-cs-fixer.phar; \
	chmod a+x php-cs-fixer.phar; \
	mv php-cs-fixer.phar /usr/local/bin/php-cs-fixer

# Install ApiGen.
RUN wget http://apigen.org/apigen.phar; \
	chmod +x apigen.phar; \
	mv apigen.phar /usr/local/bin/apigen

# Install Phing.
RUN wget http://www.phing.info/get/phing-latest.phar; \
	chmod +x phing-latest.phar; \
	mv phing-latest.phar /usr/local/bin/phing

# Purge build dependencies.
RUN apt-get purge -y curl git wget

# Clean APT.
RUN apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Add /config.
ADD config/ /config/

# Add /scripts.
ADD scripts/ /scripts/

# Add /bin.
ADD run.sh /bin/run.sh

# Configure executable.
ENTRYPOINT ["sh", "/bin/run.sh"]

# Define default command.
CMD []
