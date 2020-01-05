#
#                    ##        .
#              ## ## ##       ==
#           ## ## ## ##      ===
#       /""""""""""""""""\___/ ===
#  ~~~ {~~ ~~~~ ~~~ ~~~~ ~~ ~ /  ===- ~~~
#       \______ o          __/
#         \    \        __/
#          \____\______/
#
#          |          |
#       __ |  __   __ | _  __   _
#      /  \| /  \ /   |/  / _\ |
#      \__/| \__/ \__ |\_ \__  |
#
# Dockerfile for ISPConfig with MariaDB database
#
# https://www.howtoforge.com/tutorial/perfect-server-ubuntu-18.04-with-apache-php-myqsl-pureftpd-bind-postfix-doveot-and-ispconfig/
#

ARG BASEIMAGE=phusion/baseimage:0.11
FROM ${BASEIMAGE} as buildstage1

LABEL maintainer="Marcel Hofer <m.hofer117@gmail.com>"
LABEL version="0.4"

# Let the container know that there is no tty
ENV DEBIAN_FRONTEND noninteractive

# get basic utilities and configurations
RUN install_clean screenfetch moreutils wget curl traceroute iputils-ping dnsutils sudo rsync nano vim-nox expect \
    && echo "export TERM=xterm" >> /root/.bashrc \
    && echo ":set mouse=" > /root/.vimrc \
    && echo "syntax on" >> /root/.vimrc

# --- 2. Update Your Linux Installation
RUN apt-get -y update \
    && apt-get -y upgrade


# --- 3. Change the Default Shell
RUN echo "dash  dash/sh boolean no" | debconf-set-selections \
    && dpkg-reconfigure dash


# --- 4. Disable AppArmor (not required for phusion/baseimage)
# RUN apt-get -y remove apparmor apparmor-utils


# --- 5. Synchronize the System Clock (not possible within docker)
# RUN install_clean ntp ntpdate


# --- 6. Install Postfix, Dovecot, MariaDB, rkhunter, and binutils


# ---- 6.1 Install MariaDB, rkhunter, and binutils
RUN echo 'mysql-server mysql-server/root_password password pass' | debconf-set-selections \
    && echo 'mysql-server mysql-server/root_password_again password pass' | debconf-set-selections \
    && echo 'mariadb-server mariadb-server/root_password password pass' | debconf-set-selections \
    && echo 'mariadb-server mariadb-server/root_password_again password pass' | debconf-set-selections \
    && install_clean mariadb-client mariadb-server openssl rkhunter binutils sudo \
    && sed -i '/^bind-address/s/^/#/g' /etc/mysql/mariadb.conf.d/50-server.cnf \
    && sed -i "s/^password =.*$/password = pass/g" /etc/mysql/debian.cnf


# ---- 6.2 Install Postfix, Dovecot
RUN install_clean postfix postfix-mysql postfix-doc getmail4 dovecot-imapd dovecot-pop3d dovecot-mysql dovecot-sieve \
    dovecot-lmtpd \
    && mv /etc/postfix/master.cf /etc/postfix/master.cf.original


# --- 7. Install Amavisd-new, SpamAssassin, and Clamav
RUN install_clean amavisd-new spamassassin clamav clamav-daemon unzip bzip2 arj nomarch lzop cabextract \
    apt-listchanges libnet-ldap-perl libauthen-sasl-perl clamav-docs daemon libio-string-perl libio-socket-ssl-perl \
    libnet-ident-perl zip libnet-dns-perl postgrey patch \
    && cd /tmp \
    && wget https://git.ispconfig.org/ispconfig/ispconfig3/raw/stable-3.1/helper_scripts/ubuntu-amavisd-new-2.11.patch \
    && cd /usr/sbin \
    && cp -pf amavisd-new amavisd-new_bak \
    && patch < /tmp/ubuntu-amavisd-new-2.11.patch \
    && rm -f /tmp/ubuntu-amavisd-* \
    && freshclam


# --- 7.1 Install Metronome XMPP Server (optional), not working at the moment, so disabled
#RUN install_clean git lua5.1 liblua5.1-0-dev lua-filesystem libidn11-dev libssl-dev lua-zlib lua-expat lua-event \
#    lua-bitop lua-socket lua-sec luarocks luarocks gcc \
#    && luarocks install lpc \
#    && adduser --no-create-home --disabled-login --gecos 'Metronome' metronome \
#    && cd /opt \
#    && git clone https://github.com/maranda/metronome.git metronome \
#    && cd /opt/metronome \
#    && ./configure --ostype=debian --prefix=/usr \
#    && make \
#    && make install

# --- 7.1 from ISPConfig v3.2 onwards we could use prosody, see: https://git.ispconfig.org/ispconfig/ispconfig3/merge_requests/759
#RUN install_clean git gcc make libssl-dev prosody luarocks mercurial lua-event lua-zlib lua-dbi-mysql \
#    && luarocks install luasec \
#    && luarocks install lpty \
#    && luarocks install bit32 \
#    && mkdir -p /usr/local/lib/prosody/modules \
#    && cd /usr/local/lib/prosody/modules \
#    && hg clone https://hg.prosody.im/prosody-modules/


# --- 8. Install Apache, PHP, phpMyAdmin, FCGI, SuExec, Pear, and mcrypt
RUN echo 'phpmyadmin phpmyadmin/dbconfig-install boolean true' | debconf-set-selections \
    && echo 'phpmyadmin phpmyadmin/mysql/admin-pass password pass' | debconf-set-selections \
    && echo 'phpmyadmin phpmyadmin/reconfigure-webserver multiselect apache2' | debconf-set-selections \
    && service mysql start \
    && add-apt-repository -y ppa:ondrej/php \
    && install_clean apache2 apache2-doc apache2-utils libapache2-mod-php7.2 php7.2 php7.2-common php7.2-gd php7.2-mysql \
    php7.2-imap phpmyadmin php7.2-cli php7.2-cgi libapache2-mod-fcgid apache2-suexec-pristine mcrypt \
    imagemagick libruby libapache2-mod-python php7.2-curl php7.2-intl php7.2-pspell php7.2-recode php7.2-sqlite3 \
    php7.2-tidy php7.2-xmlrpc php7.2-xsl memcached php7.2-memcache php7.2-imagick php7.2-gettext php7.2-zip php7.2-mbstring \
    php7.2-soap \
    && a2enmod suexec rewrite ssl actions include cgi proxy proxy_http \
    && a2enmod dav_fs dav auth_digest headers \
    && sed -i '/^#application\/x-ruby/s/^#//g' /etc/mime.types \
    # manually install a recent version of phpMyAdmin
    && cd /usr/share \
    && rm -rf phpmyadmin \
    && wget https://files.phpmyadmin.net/phpMyAdmin/4.8.5/phpMyAdmin-4.8.5-all-languages.zip \
    && unzip phpMyAdmin-4.8.5-all-languages.zip \
    && rm -f phpMyAdmin-4.8.5-all-languages.zip \
    && mv phpMyAdmin-4.8.5-all-languages phpmyadmin \
    && cd /usr/share/phpmyadmin/ \
    && mkdir -p tmp \
    && chown www-data:www-data tmp \
    && sed -i "s/^define('CONFIG_DIR', '');$/define('CONFIG_DIR', '\/etc\/phpmyadmin\/');/g" libraries/vendor_config.php \
    && echo -e "<?php\n\$cfg['AuthLog']=\"php\";\n" > /etc/phpmyadmin/conf.d/authlog.php

# ---- 8.1 PHP Opcode cache (optional)
RUN install_clean php7.2-opcache php7.2-apcu


# ---- 8.2 PHP-FPM
RUN install_clean php7.2-fpm \
    && a2enmod actions proxy_fcgi alias


# ---- 8.3 Install HHVM (HipHop Virtual Machine), optional
RUN install_clean hhvm


# --- 9. Install Let's Encrypt
RUN install_clean certbot


# --- 10. Install Mailman
RUN echo 'mailman mailman/default_server_language en' | debconf-set-selections \
    && install_clean mailman \
#    && newlist -q mailman mail@mail.com pass \
    && mv /etc/aliases /etc/aliases.original \
    && ln -s /etc/mailman/apache.conf /etc/apache2/conf-available/mailman.conf \
    && a2enconf mailman


# --- 11. Install PureFTPd and Quota
FROM ${BASEIMAGE} as pureftpdbuild
# compile from source to disable capabilities (not working in docker)
RUN install_clean dpkg-dev debhelper openbsd-inetd debian-keyring \
    && apt-get update \
    && apt-get -y -qq build-dep pure-ftpd \
    && mkdir /tmp/pure-ftpd-mysql/ \
    && cd /tmp/pure-ftpd-mysql/ \
    # fix error with permissions during download
    && chown -R _apt /tmp/pure-ftpd-mysql \
    # download sources
    && apt-get -qq source pure-ftpd \
    # build packages
    && cd /tmp/pure-ftpd-mysql/pure-ftpd* \
    && sed -i '/^optflags=/ s/$/ --without-capabilities/g' ./debian/rules \
    # dpkg-buildpackage -b -uc \
    && dpkg-buildpackage -b -uc > /tmp/pureftpd-build-stdout.txt 2> /tmp/pureftpd-build-stderr.txt \
    && mv /tmp/pure-ftpd-mysql/pure-ftpd-common_*.deb /tmp/pure-ftpd-mysql/pure-ftpd-mysql_*.deb /srv/ \
    # clean up
    && cd /tmp/ \
    && rm -rf /tmp/pure-ftpd-mysql/ \
    && /bd_build/cleanup.sh

FROM buildstage1 as buildstage2
COPY --from=pureftpdbuild /srv/pure-ftpd-*.deb /tmp/
RUN \
    # install the new deb files
    install_clean /tmp/pure-ftpd-common_*.deb /tmp/pure-ftpd-mysql_*.deb \
    # Prevent pure-ftpd upgrading
    && apt-mark hold pure-ftpd-common pure-ftpd-mysql \
    # clean up
    && rm -rf /tmp/pure-ftpd-* \
    # install quota, required quota support on the docker-host?
    && install_clean quota quotatool \
    # setup ftpgroup and ftpuser
    && groupadd ftpgroup \
    && useradd -g ftpgroup -d /dev/null -s /etc ftpuser \
    # configuration
    && echo "30000 30009" > /etc/pure-ftpd/conf/PassivePortRange \
    && sed -i "s/^STANDALONE_OR_INETD=.*$/STANDALONE_OR_INETD=standalone/g" /etc/default/pure-ftpd-common \
    && sed -i "s/^VIRTUALCHROOT=.*$/VIRTUALCHROOT=true/g" /etc/default/pure-ftpd-common \
    && echo 0 > /etc/pure-ftpd/conf/TLS \
    # clean up
    && /bd_build/cleanup.sh
    # enable TLS
#    && echo 0 > /etc/pure-ftpd/conf/TLS \
#    && mkdir -p /etc/ssl/private/ \
#    && openssl req -x509 -nodes -days 7300 -newkey rsa:2048 -keyout /etc/ssl/private/pure-ftpd.pem \
#    -out /etc/ssl/private/pure-ftpd.pem \
#    -subj "/C=GB/ST=London/L=London/O=Global Security/OU=IT Department/CN=ispconfig.local" \
#    && chmod 600 /etc/ssl/private/pure-ftpd.pem

# --- 12. Install BIND DNS Server
RUN install_clean bind9 dnsutils haveged


# --- 13. Install Vlogger, Webalizer, and AWStats
RUN install_clean vlogger webalizer awstats geoip-database libclass-dbi-mysql-perl \
    # comment all lines
    && sed -i 's/^\([^#].*\)/#\1/g' /etc/cron.d/awstats


# --- 14. Install Jailkit
FROM ${BASEIMAGE} as jailkitbuild
RUN install_clean build-essential autoconf automake libtool flex bison debhelper binutils wget python \
    && cd /tmp \
    && wget http://olivier.sessink.nl/jailkit/jailkit-2.20.tar.gz \
    && tar xvfz jailkit-*.tar.gz \
    && cd jailkit-* \
    && echo 5 > debian/compat \
    && ./debian/rules binary \
    && cd /tmp \
    && mv /tmp/jailkit_*.deb /srv/ \
    # clean up
    && /bd_build/cleanup.sh

FROM buildstage2 as buildstage3
COPY --from=jailkitbuild /srv/jailkit_*.deb /tmp/
RUN \
    # install the new deb files
    install_clean /tmp/jailkit_*.deb \
    # clean up
    && /bd_build/cleanup.sh


# --- 15. Install fail2ban and UFW
# replaced by CSF / LFD
#RUN install_clean fail2ban
#ADD ./etc/fail2ban/jail.local /etc/fail2ban/jail.local
#ADD ./etc/fail2ban/filter.d/pureftpd.conf /etc/fail2ban/filter.d/pureftpd.conf
#ADD ./etc/fail2ban/filter.d/dovecot-pop3imap.conf /etc/fail2ban/filter.d/dovecot-pop3imap.conf
#RUN echo "ignoreregex =" >> /etc/fail2ban/filter.d/postfix-sasl.conf
#RUN install_clean ufw


# --- 16. Install Roundcube Webmail
RUN service mysql start \
    && install_clean roundcube roundcube-core roundcube-mysql roundcube-plugins javascript-common \
    libjs-jquery-mousewheel php-net-sieve tinymce \
    && a2enconf roundcube \
    && sed -i '/^<Directory \/var\/lib\/roundcube\/>$/a \ \ AddType application\/x-httpd-php .php' \
    /etc/apache2/conf-available/roundcube.conf \
    && sed -i '/^<Directory \/var\/lib\/roundcube\/>$/i Alias \/webmail \/var\/lib\/roundcube' \
    /etc/apache2/conf-available/roundcube.conf \
    && sed -i "s/^\$config\['default_host'\] =.*$/\$config\['default_host'\] = 'localhost';/g" \
    /etc/roundcube/config.inc.php


# --- 17. Install ISPConfig 3.1
RUN cd /root \
    && wget -O ispconfig.tar.gz \
    https://git.ispconfig.org/ispconfig/ispconfig3/repository/archive.tar.gz?ref=stable-3.1 \
    && tar xfz ispconfig.tar.gz \
    && cd ispconfig3*/install/ \
    # hack to allow pre-munted ispconfig volume in docker
    && sed -i "s/is_dir('\/usr\/local\/ispconfig')/is_dir('\/usr\/local\/ispconfig\/interface')/g" install.php


# --- CUSTOM: additional php versions
RUN install_clean php5.6 php5.6-cli php5.6-cgi php5.6-fpm \
    php5.6-bz2 \
    php5.6-cgi \
    php5.6-cli \
    php5.6-common \
    php5.6-curl \
    php5.6-fpm \
    php5.6-gd \
    php5.6-imap \
    php5.6-intl \
    php5.6-json \
    php5.6-mbstring \
    php5.6-mcrypt \
    php5.6-mysql \
    php5.6-opcache \
    php5.6-pspell \
    php5.6-readline \
    php5.6-recode \
    php5.6-soap \
    php5.6-sqlite3 \
    php5.6-tidy \
    php5.6-xml \
    php5.6-xmlrpc \
    php5.6-xsl \
    php5.6-zip

RUN install_clean php7.0 php7.0-cli php7.0-cgi php7.0-fpm \
    php7.0-bz2 \
    php7.0-cgi \
    php7.0-cli \
    php7.0-common \
    php7.0-curl \
    php7.0-fpm \
    php7.0-gd \
    php7.0-imap \
    php7.0-intl \
    php7.0-json \
    php7.0-mbstring \
    php7.0-mcrypt \
    php7.0-mysql \
    php7.0-opcache \
    php7.0-pspell \
    php7.0-readline \
    php7.0-recode \
    php7.0-soap \
    php7.0-sqlite3 \
    php7.0-tidy \
    php7.0-xml \
    php7.0-xmlrpc \
    php7.0-xsl \
    php7.0-zip

RUN install_clean php7.1 php7.1-cli php7.1-cgi php7.1-fpm \
    php7.1-bz2 \
    php7.1-cgi \
    php7.1-cli \
    php7.1-common \
    php7.1-curl \
    php7.1-fpm \
    php7.1-gd \
    php7.1-imap \
    php7.1-intl \
    php7.1-json \
    php7.1-mbstring \
    php7.1-mcrypt \
    php7.1-mysql \
    php7.1-opcache \
    php7.1-pspell \
    php7.1-readline \
    php7.1-recode \
    php7.1-soap \
    php7.1-sqlite3 \
    php7.1-tidy \
    php7.1-xml \
    php7.1-xmlrpc \
    php7.1-xsl \
    php7.1-zip

RUN install_clean php7.2 php7.2-cli php7.2-cgi php7.2-fpm \
    php7.2-bz2 \
    php7.2-cgi \
    php7.2-cli \
    php7.2-common \
    php7.2-curl \
    php7.2-fpm \
    php7.2-gd \
    php7.2-imap \
    php7.2-intl \
    php7.2-json \
    php7.2-mbstring \
    php7.2-mysql \
    php7.2-opcache \
    php7.2-pspell \
    php7.2-readline \
    php7.2-recode \
    php7.2-soap \
    php7.2-sqlite3 \
    php7.2-tidy \
    php7.2-xml \
    php7.2-xmlrpc \
    php7.2-xsl \
    php7.2-zip

RUN update-alternatives --set php /usr/bin/php7.2 \
    && update-alternatives --set php-cgi /usr/bin/php-cgi7.2 \
    && update-alternatives --set php-cgi-bin /usr/lib/cgi-bin/php7.2 \
    && rm -f /etc/php/*/fpm/pool.d/www.conf


# --- CUSTOM: install ioncube loaders
RUN cd /tmp \
    && wget https://downloads.ioncube.com/loader_downloads/ioncube_loaders_lin_x86-64.tar.gz \
    && tar -xzf ioncube_loaders_lin_x86-64.tar.gz -C /usr/local \
    && rm -f /tmp/ioncube* \
    && echo "zend_extension=/usr/local/ioncube/ioncube_loader_lin_5.6.so" > /etc/php/5.6/mods-available/ioncube.ini \
    && ln -s /etc/php/5.6/mods-available/ioncube.ini /etc/php/5.6/cgi/conf.d/10-ioncube.ini \
    && ln -s /etc/php/5.6/mods-available/ioncube.ini /etc/php/5.6/cli/conf.d/10-ioncube.ini \
    && ln -s /etc/php/5.6/mods-available/ioncube.ini /etc/php/5.6/fpm/conf.d/10-ioncube.ini \
    && echo "zend_extension=/usr/local/ioncube/ioncube_loader_lin_7.0.so" > /etc/php/7.0/mods-available/ioncube.ini \
    && ln -s /etc/php/7.0/mods-available/ioncube.ini /etc/php/7.0/cgi/conf.d/10-ioncube.ini \
    && ln -s /etc/php/7.0/mods-available/ioncube.ini /etc/php/7.0/cli/conf.d/10-ioncube.ini \
    && ln -s /etc/php/7.0/mods-available/ioncube.ini /etc/php/7.0/fpm/conf.d/10-ioncube.ini \
    && echo "zend_extension=/usr/local/ioncube/ioncube_loader_lin_7.1.so" > /etc/php/7.1/mods-available/ioncube.ini \
    && ln -s /etc/php/7.1/mods-available/ioncube.ini /etc/php/7.1/cgi/conf.d/10-ioncube.ini \
    && ln -s /etc/php/7.1/mods-available/ioncube.ini /etc/php/7.1/cli/conf.d/10-ioncube.ini \
    && ln -s /etc/php/7.1/mods-available/ioncube.ini /etc/php/7.1/fpm/conf.d/10-ioncube.ini \
    && echo "zend_extension=/usr/local/ioncube/ioncube_loader_lin_7.2.so" > /etc/php/7.2/mods-available/ioncube.ini \
    && ln -s /etc/php/7.2/mods-available/ioncube.ini /etc/php/7.2/cgi/conf.d/10-ioncube.ini \
    && ln -s /etc/php/7.2/mods-available/ioncube.ini /etc/php/7.2/cli/conf.d/10-ioncube.ini \
    && ln -s /etc/php/7.2/mods-available/ioncube.ini /etc/php/7.2/fpm/conf.d/10-ioncube.ini


# --- CUSTOM: install csf
RUN install_clean iptables libgd-graph-perl libio-socket-ssl-perl libcrypt-ssleay-perl libnet-libidn-perl \
    libio-socket-inet6-perl libsocket6-perl libwww-perl \
    && cd /usr/src \
    && rm -fv csf.tgz \
    && wget https://download.configserver.com/csf.tgz \
    && tar -xzf csf.tgz \
    && cd csf \
    && sh install.sh \
    && cd /usr/src \
    && rm -rf csf* \
#    && perl /usr/local/csf/bin/csftest.pl
    # enable UI and open all ports (docker will nat only those you wish anyway)
    && sed -i "s/^UI = \"0\"$/UI = \"1\"/g" /etc/csf/csf.conf \
    && sed -i "s/^TESTING = \"1\"$/TESTING = \"0\"/g" /etc/csf/csf.conf \
    && sed -i "s/^UI_PORT = \"6666\"$/UI_PORT = \"7443\"/g" /etc/csf/csf.conf \
    && sed -i "/^\(TCP_IN\|TCP6_IN\) = \".*\"$/ {s/\"\(.*\)\"/\"1:65535\"/}" /etc/csf/csf.conf \
    && sed -i "/^\(UDP_IN\|UDP6_IN\) = \".*\"$/ {s/\"\(.*\)\"/\"1:65535\"/}" /etc/csf/csf.conf


# --- CUSTOM: install maldet
RUN cd /tmp/ \
    && wget https://www.rfxn.com/downloads/maldetect-current.tar.gz \
    && tar xfz maldetect-current.tar.gz \
    && rm -f maldetect-current.tar.gz \
    && cd maldetect-* \
    && chmod +x install.sh \
    && ./install.sh \
    && cd / \
    && rm -rf /tmp/maldetect-*


# --- CUSTOM: install incrond
RUN install_clean incron \
    && echo 'root' >> /etc/incron.allow \
    && mkdir -p /etc/incron.d

# --- run update again / CLEANING
RUN apt-get -y update \
    && apt-get -y upgrade \
    && apt-get autoremove -y \
    && /bd_build/cleanup.sh
RUN freshclam || true

# --- CUSTOM: add all scripts / configs / executables
COPY rootfs /
RUN a2enconf httpoxy \
    && newaliases \
    && chmod 500 /etc/my_init.d/*.sh \
    && chmod 500 /etc/service/*/run \
    && chmod 500 /scripts/*.sh /scripts/**/*.sh \
    && chmod 500 /etc/cron.hourly/*.sh \
    && chmod 500 /etc/cron.daily/*.sh \
    && chmod 755 /usr/bin/systemctl /usr/sbin/service /entrypoint.sh \
    && touch /uninitialized

# --- CUSTOM: create required directories
RUN touch /root/.rnd \
    && rmdir /var/backups \
    && mkdir -p /var/backup/sql \
    && mkdir -p /var/backup/.etc \
    && mkdir -p /var/log/ispconfig/httpd \
    && mkdir -p /var/www/html \
    && mkdir -p /var/run/clamav \
    && mkdir -p /var/run/mailman \
    #&& mkdir -p /var/log/metronome \
    #&& mkdir -p /var/run/prosody \
    && mkdir -p /run/named \
    && chown clamav:clamav /var/run/clamav \
    && chown list:list /var/run/mailman
    #&& chown metronome:metronome /var/log/metronome \
    #&& chown prosody:prosody /var/run/prosody \
    #&& chown named:named /run/named

# Give children processes 10 seconds to timeout
ENV KILL_PROCESS_TIMEOUT=10
# Give all other processes (such as those which have been forked) 30 seconds to timeout
ENV KILL_ALL_PROCESSES_TIMEOUT=30

EXPOSE 20/tcp 21/tcp 22/tcp 53/tcp 53/udp 80/tcp 443/tcp 953/tcp 8080/tcp 30000 30001 30002 30003 30004 30005 30006 30007 30008 30009 3306

# disable volume definition here as it caused issues with the child-container (:'full')
VOLUME ["/var/lib/mysql/","/var/lib/mailman","/var/vmail","/var/www/","/usr/local/ispconfig/","/var/backup/"]

CMD ["/sbin/my_init","--","/entrypoint.sh"]
