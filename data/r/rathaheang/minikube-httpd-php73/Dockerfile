FROM debian:buster-slim

RUN apt-get update -y && \
            DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
            apache2 \
            locales \
            curl \
            bzip2 \
            openssl \
            less \
            php-apcu \
            php7.3-bcmath php7.3-bz2 php7.3-cli php7.3-common php7.3-curl \
            php7.3-gd php7.3-imap php7.3-interbase php7.3-intl php7.3-json \
            php7.3-mbstring php7.3-mysql php7.3-opcache php7.3-readline php7.3-soap \
            php7.3-xml php7.3-xmlrpc php7.3-xsl php7.3-zip libapache2-mod-php7.3

ENV TZ=Asia/Phnom_Penh
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN a2enmod actions alias expires headers rewrite ssl
RUN apt-get clean && rm -rf /var/lib/apt/lists/*

ADD docker/000-default.conf /etc/apache2/sites-available/000-default.conf
ADD docker/php.ini /etc/php/7.3/apache2/php.ini

ADD docker/Entrypoint.sh /Entrypoint.sh
ENTRYPOINT ["/Entrypoint.sh"]

WORKDIR /var/www/html

CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]
