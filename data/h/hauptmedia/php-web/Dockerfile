FROM	hauptmedia/php:7.0

ENV     DEBIAN_FRONTEND noninteractive

RUN     apt-get update -qq && \
        apt-get install -y \
        apache2 php7.0 && \
        apt-get clean autoclean && \
        apt-get autoremove --yes && \
        rm -rf /var/lib/{apt,dpkg,cache,log}/

EXPOSE	80 443

CMD	["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]
