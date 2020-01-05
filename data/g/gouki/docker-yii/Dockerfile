FROM debian:latest
MAINTAINER gouki <gouki.xiao@gmail.com>

ENV DEBIAN_FRONTEND noninteractive

WORKDIR /root

RUN \
  buildDeps='busybox git curl supervisor apache2 php7.2 php7.2-opcache php7.2-mysql php7.2-sqlite3 php7.2-curl php7.2-gd php7.2-json php7.2-mbstring php7.2-zip php7.2-xml libapache2-mod-php' \

  && sed -i 's/deb.debian.org/mirrors.ustc.edu.cn/g' /etc/apt/sources.list  \

  && apt-get update \
  && apt-get -y install wget apt-transport-https lsb-release ca-certificates \
  && wget -O /etc/apt/trusted.gpg.d/php.gpg https://packages.sury.org/php/apt.gpg \
  && sh -c 'echo "deb https://packages.sury.org/php/ $(lsb_release -sc) main" > /etc/apt/sources.list.d/php.list'  \

  && apt-get update \
  && apt-get -y install $buildDeps \

  && a2enmod rewrite \

  && php -r "readfile('https://getcomposer.org/installer');" > composer-setup.php  \
  && php composer-setup.php --install-dir=/usr/local/bin --filename=composer  \
  && php -r "unlink('composer-setup.php');"   \
  && /usr/local/bin/composer config -g repo.packagist composer https://packagist.phpcomposer.com \
  && /usr/local/bin/composer global require hirak/prestissimo \
  && /usr/local/bin/composer global require "fxp/composer-asset-plugin:*" \

  && apt-get clean \
#  && apt-get purge -y --auto-remove $buildDeps \
  && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /var/cache/apt/archive/*.deb /root/.cache/composer/*


VOLUME ["/var/www/html","/server/wwwroot"]

# Adding ressources
#ADD ressources/apache-config.conf /etc/apache2/sites-enabled/000-default.conf

COPY resources/start.sh /root/start.sh
COPY resources/run.sh   /root/run.sh
COPY resources/apache.conf /etc/supervisor/conf.d/all.conf

RUN chmod 755 /root/*.sh

#CMD ["/usr/bin/supervisord"]

#COPY docker-entrypoint.sh /
#ENTRYPOINT ["/docker-entrypoint.sh"]

#ENTRYPOINT ["/etc/init.d/apache2", "restart"]

CMD ["/root/run.sh"]



EXPOSE 80