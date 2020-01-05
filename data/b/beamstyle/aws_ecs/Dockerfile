FROM php:7.3-cli

MAINTAINER Thomas Cheng <thomas@beamstyle.com.hk>

# Reference DockerFile: https://github.com/meanbee/docker-magento2



# pdftk fix
# Fix the following weird error when installing pdftk
# update-alternatives: error: error creating symbolic link '/usr/share/man/man1/rmid.1.gz.dpkg-tmp': No such file or directory
RUN mkdir -p /usr/share/man/man1



# Install dependencies
RUN set -eux;                               \
    apt-get update && apt-get install -y    \
                                            \
        `# Generate dependencies`           \
        cron                                \
        default-mysql-client                \
        git                                 \
        libmcrypt-dev                       \
        libxslt1-dev                        \
        libzip-dev                          \
        pdftk                               \
        rsyslog                             \
        sudo                                \
        unzip                               \
        zlib1g-dev                          \
                                            \
        `# GD library`                      \
        libfreetype6-dev                    \
        libjpeg62-turbo-dev                 \
        libpng-dev                          \
        libwebp-dev                         \
        libxpm-dev                          \
                                            \
        `# Intl library`                    \
        libicu-dev                          \
                                            \
        `# htpasswd`                        \
        apache2-utils                       \
                                            \
        `# Handy utilities`                 \
        openssh-server                      \
        vim                                 \
                                            \
    `# Remove unwanted files`               \
    && rm -rf /var/lib/apt/lists/*



RUN set -eux;                               \
    `# General PHP extensions`              \
    docker-php-ext-install                  \
        bcmath                              \
        dom                                 \
        intl                                \
        mbstring                            \
        opcache                             \
        pdo_mysql                           \
        soap                                \
        tokenizer                           \
        xsl                                 \
        zip                                 \
                                            \
    `# mysqli library`                      \
    && docker-php-ext-install mysqli        \
    && docker-php-ext-enable mysqli         \
                                            \
    `# mcrypt library`                      \
    && pecl install mcrypt-1.0.2            \
    && docker-php-ext-enable mcrypt         \
                                            \
    `# GD library`                          \
    && docker-php-ext-configure gd          \
        --enable-gd-native-ttf              \
        --enable-gd-jis-conv                \
        --with-freetype-dir=/usr/include/   \
        --with-jpeg-dir=/usr/include/       \
        --with-png-dir=/usr/include/        \
        --with-webp-dir=/usr/include/       \
        --with-xpm-dir=/usr/include/        \
    && docker-php-ext-install gd



# Opcache settings
RUN set -eux;                                                                                                                   \
    `# Copy opcache production settings`                                                                                        \
    cp "$PHP_INI_DIR/php.ini-production" "$PHP_INI_DIR/php.ini"                                                                 \
                                                                                                                                \
    `# Configure opcache`                                                                                                       \
    && sed -i 's/;opcache\.enable=[01]$/opcache.enable=1/g'                                             $PHP_INI_DIR/php.ini    \
    && sed -i 's/;opcache\.enable_cli=[01]$/opcache.enable_cli=1/g'                                     $PHP_INI_DIR/php.ini    \
    && sed -i 's/;opcache\.interned_strings_buffer=[1-9][0-9].*$/opcache.interned_strings_buffer=8/g'   $PHP_INI_DIR/php.ini    \
    && sed -i 's/;opcache\.max_accelerated_files=[1-9][0-9].*$/opcache.max_accelerated_files=10000/g'   $PHP_INI_DIR/php.ini    \
    && sed -i 's/;opcache\.memory_consumption=[1-9][0-9].*$/opcache.memory_consumption=128/g'           $PHP_INI_DIR/php.ini    \
    && sed -i 's/;opcache\.save_comments=[01]$/opcache.save_comments=1/g'                               $PHP_INI_DIR/php.ini    \
    && sed -i 's/;opcache\.revalidate_freq=[1-9][0-9].*$/opcache.revalidate_freq=2/g'                   $PHP_INI_DIR/php.ini



# Get composer installed to /usr/local/bin/composer
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer



# Configure SSH server

RUN mkdir /var/run/sshd

# Enabling password-based login for SSH server
RUN sed -ri 's/#PermitRootLogin.*$/PermitRootLogin yes/g' /etc/ssh/sshd_config
RUN sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config

# Login fix (otherwise user is kicked off after login) for SSH server
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd

# Set user visibility
ENV NOTVISIBLE "in users profile"
RUN echo "export VISIBLE=now" >> /etc/profile

# Exposing the SSH port
EXPOSE 22



# Environment variables
ENV SRC_ROOT                    "/var/www/html"
ENV SRC_GIT_REPOSITORY_URL      "https://sample-username:sample-secret@bitbucket.org/sample-organization/sample-project.git"
ENV SRC_GIT_REPOSITORY_BRANCH   ""

ENV COMPOSER_ALLOW_SUPERUSER    1
ENV COMPOSER_GITHUB_TOKEN       ""
ENV COMPOSER_BITBUCKET_KEY      ""
ENV COMPOSER_BITBUCKET_SECRET   ""
ENV COMPOSER_ROOT               "/var/www/html/_laravel"

ENV SSH_ROOT_PASSWORD           ""
ENV SSH_HOME_DIRECTORY          "/var/www/html"

ENV LARAVEL_ROOT                "/var/www/html/_laravel"
ENV LARAVEL_BASIC_AUTH_USERNAME ""
ENV LARAVEL_BASIC_AUTH_PASSWORD ""
ENV LARAVEL_ENV_FILE            ""
ENV LARAVEL_PHP_BIN             "/usr/local/bin/php"

ENV CRON_SCRIPT_PATH            "/var/www/html/_scripts/cron-production.sh"
ENV CRON_SCRIPT_ARGUMENTS       "/usr/local/bin/php"
ENV CRON_SCHEDULE               "* * * * *"
ENV CRON_LOG                    "/var/www/html/_laravel/storage/logs/cron.log"



# Execute script start.sh
ADD start.sh /usr/local/bin/
RUN ["chmod", "+x", "/usr/local/bin/start.sh"]
CMD ["/usr/local/bin/start.sh"]
