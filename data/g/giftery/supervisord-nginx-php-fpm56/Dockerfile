# rebuild: 2019011401
FROM centos:7
MAINTAINER Evgenii Tereshkov <e.tereshkov@southbridge.ru>

RUN echo "Start!" && \
    rpm -Uvh http://rpms.southbridge.ru/southbridge-rhel7-stable.rpm && \
    yum -y install epel-release southbridge-php56-release && \
    yum -y install supervisor bash cronie ssmtp nginx wget zip bzip2 p7zip php php-fpm php-xdebug php-opcache php-mcrypt php-gd php-mbstring php-intl php-mysqlnd php-pdo php-xml php-pecl-zip php-process php-pecl-redis-2.2.7 php-bcmath php-soap && \
    (echo; echo "opcache.enable_cli=1") >> /etc/php.d/10-opcache.ini && \
    rm -fr /var/cache/*; rm -f /etc/php.d/15-xdebug.ini && \
    mkdir -p /var/cache/nginx && mkdir -p /run/php-fpm && \
    localedef -i ru_RU -f UTF-8 ru_RU.UTF-8 && \
    for x in `ls /usr/share/locale | grep -v -e ^en -e ^ru -e ^locale`; do rm -fr /usr/share/locale/$x; done && \
    for x in `ls /usr/share/i18n/locales/ | grep -v -e ^en -e ^ru`; do rm -fr /usr/share/i18n/locales/$x; done && \
    rm -fr /usr/share/locale/ca* /usr/share/locale/den /usr/share/locale/men /usr/share/locale/wen /usr/share/locale/zen && \
    cd /usr/lib/locale && localedef --list-archive | grep -v -e ^en -e ^ru | xargs localedef --delete-from-archive && \
    mv -f locale-archive locale-archive.tmpl && \
    build-locale-archive && \
    rm -f /etc/localtime && \
    ln -s /usr/share/zoneinfo/Europe/Moscow /etc/localtime && \
    echo "date.timezone = Europe/Moscow" > /etc/php.d/991-timezone.ini && \
    yum -y install qtwebkit cabextract xorg-x11-font-utils php-pecl-geoip && \
    mkdir /tmp/wkhtmltopdf && \
    cd /tmp/wkhtmltopdf && \
    wget -q https://downloads.wkhtmltopdf.org/obsolete/linux/wkhtmltopdf-0.10.0_rc2-static-amd64.tar.bz2 && \
    tar jxf wkhtmltopdf-0.10.0_rc2-static-amd64.tar.bz2 && \
    mv wkhtmltopdf-amd64 /usr/bin/wkhtmltopdf && \
    rpm -i https://downloads.sourceforge.net/project/mscorefonts2/rpms/msttcore-fonts-installer-2.6-1.noarch.rpm && \
    rm -fr /usr/share/{backgrounds,httpd,doc,man,groff,info,lintian,linda,kde4,icons,licenses}/* /var/cache/man/* && \
    yum clean all && \
    echo "Done install..."

##
# Add Project files like nginx and php-fpm processes and configs
# Also custom scripts and bashrc
##
COPY system-root/ /

ENV TERM="xterm" \
    DB_HOST="" \
    DB_NAME="" \
    DB_USER=""\
    DB_PASSWORD=""\
    # Set defaults which can be overriden
    DB_PORT="3306" \
    # Set defaults for redis
    REDIS_PORT="6379" \
    REDIS_DATABASE="0" \
    REDIS_SCHEME="tcp" \
    # Cronlock is used to stop simultaneous cronjobs in clusterised environments
    CRONLOCK_HOST="" \
    # This is for your project root
    PROJECT_ROOT="/srv/www/php-app"\
    # This is used by nginx and php-fpm
    WEB_ROOT="/srv/www/php-app/htdocs"\
    # This can be overidden by you, it's just default for us
    TZ="Europe/Moscow"

WORKDIR /srv/www/php-app
EXPOSE 80
ENTRYPOINT ["/docker-entrypoint.sh"]
