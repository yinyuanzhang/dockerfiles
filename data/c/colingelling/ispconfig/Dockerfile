FROM debian:stretch-slim

MAINTAINER Colin <colin@splanet.nl> version: 1.0

# Arguments
ARG BUILD_ISPCONFIG="ISPConfig-3-stable"
ARG BUILD_ROUNDCUBE="1.1.6"
ARG MYSQL_ROOT_PWD="pass"

# Let the container know that there is no tty
ENV DEBIAN_FRONTEND noninteractive

# --- 1 Preliminary
RUN apt-get -y update && apt-get -y upgrade && apt-get -y install apt-utils rsyslog rsyslog-relp logrotate supervisor screenfetch

# Create the log file to be able to run tail
RUN touch /var/log/cron.log /var/log/auth.log

# Install the SSH server
RUN apt-get -y install ssh openssh-server

# Install a shell text editor
RUN apt-get -y install nano vim-nox

# Update Your Debian Installation
ADD ./etc/apt/sources.list /etc/apt/sources.list
RUN apt-get -y update && apt-get -y upgrade

# Change The Default Shell
RUN echo "dash dash/sh boolean no" | debconf-set-selections && dpkg-reconfigure dash

RUN apt-get -y install ntp

# Install Postfix, Dovecot, MySQL, phpMyAdmin, rkhunter, binutils
RUN echo "mariadb-server  mariadb-server/root_password_again password ${MYSQL_ROOT_PWD}" | debconf-set-selections
RUN echo "mariadb-server  mariadb-server/root_password password ${MYSQL_ROOT_PWD}" | debconf-set-selections
RUN echo "mariadb-server-10.0 mysql-server/root_password password ${MYSQL_ROOT_PWD}" | debconf-set-selections
RUN echo "mariadb-server-10.0 mysql-server/root_password_again password ${MYSQL_ROOT_PWD}" | debconf-set-selections
RUN apt-get -y install postfix postfix-mysql postfix-doc mariadb-client mariadb-server openssl getmail4 rkhunter binutils dovecot-imapd dovecot-pop3d dovecot-mysql dovecot-sieve dovecot-lmtpd sudo
ADD ./etc/postfix/master.cf /etc/postfix/master.cf
RUN mv /etc/mysql/mariadb.conf.d/50-server.cnf /etc/mysql/mariadb.conf.d/50-server.cnf.backup
ADD ./etc/mysql/mariadb.conf.d/50-server.cnf /etc/mysql/mariadb.conf.d/50-server.cnf
RUN mv /etc/mysql/debian.cnf /etc/mysql/debian.cnf.backup
ADD ./etc/mysql/debian.cnf /etc/mysql/debian.cnf
ADD ./etc/security/limits.conf /etc/security/limits.conf
RUN mkdir -p /etc/systemd/system/mysql.service.d/
ADD ./etc/systemd/system/mysql.service.d/limits.conf /etc/systemd/system/mysql.service.d/limits.conf
RUN service postfix restart && service dovecot restart && service mysql restart

# Install Amavisd-new, SpamAssassin And Clamav
RUN apt-get install -y amavisd-new spamassassin clamav clamav-daemon zoo unzip bzip2 arj nomarch lzop cabextract apt-listchanges libnet-ldap-perl libauthen-sasl-perl clamav-docs daemon libio-string-perl libio-socket-ssl-perl libnet-ident-perl zip libnet-dns-perl libdbd-mysql-perl postgrey
ADD ./etc/clamav/clamd.conf /etc/clamav/clamd.conf
RUN service spamassassin stop && systemctl disable spamassassin
RUN service clamav-daemon start

# Install Metronome XMPP Server
RUN echo "deb http://packages.prosody.im/debian stretch main" > /etc/apt/sources.list.d/metronome.list
RUN wget http://prosody.im/files/prosody-debian-packages.key -O - | sudo apt-key add -
RUN apt-get -qq update && apt-get -y -qq install git lua5.1 liblua5.1-0-dev lua-filesystem libidn11-dev libssl-dev lua-zlib lua-expat lua-event lua-bitop lua-socket lua-sec luarocks
RUN luarocks install lpc
RUN adduser --no-create-home --disabled-login --gecos 'Metronome' metronome
RUN cd /opt && git clone https://github.com/maranda/metronome.git metronome
RUN cd /opt/metronome && ./configure --ostype=debian --prefix=/usr && make && make install

# Install Apache2, PHP7, phpMyAdmin, FCGI, suExec, Pear, And mcrypt
RUN echo 'phpmyadmin phpmyadmin/dbconfig-install boolean true' | debconf-set-selections \
&& echo 'phpmyadmin phpmyadmin/mysql/admin-pass password ${MYSQL_ROOT_PWD}' | debconf-set-selections \
&& echo 'phpmyadmin phpmyadmin/reconfigure-webserver multiselect apache2' | debconf-set-selections
RUN apt-get -y install apache2 apache2-doc apache2-utils libapache2-mod-php php7.0 php7.0-common php7.0-gd php7.0-mysql php7.0-imap phpmyadmin php7.0-cli php7.0-cgi libapache2-mod-fcgid apache2-suexec-pristine php-pear php7.0-mcrypt mcrypt  imagemagick libruby libapache2-mod-python php7.0-curl php7.0-intl php7.0-pspell php7.0-recode php7.0-sqlite3 php7.0-tidy php7.0-xmlrpc php7.0-xsl php-memcache php-imagick php-gettext php7.0-zip php7.0-mbstring memcached libapache2-mod-passenger php7.0-soap
RUN a2enmod suexec rewrite actions include dav_fs dav auth_digest cgi

RUN a2enmod actions proxy_fcgi alias
RUN service apache2 restart

# Install PHP Opcode Cache
RUN apt-get -y install php7.0-opcache php-apcu

# Install PureFTPd And Quota
RUN apt-get -qq -y --force-yes install dpkg-dev debhelper openbsd-inetd debian-keyring
# install dependancies
RUN apt-get -y -qq build-dep pure-ftpd
# build from source
RUN mkdir /tmp/pure-ftpd-mysql/ && \
    cd /tmp/pure-ftpd-mysql/ && \
    apt-get -qq source pure-ftpd-mysql && \
    cd pure-ftpd-* && \
    sed -i '/^optflags=/ s/$/ --without-capabilities/g' ./debian/rules && \
    dpkg-buildpackage -b -uc > /tmp/pureftpd-build-stdout.txt 2> /tmp/pureftpd-build-stderr.txt
# install the new deb files
RUN dpkg -i /tmp/pure-ftpd-mysql/pure-ftpd-common*.deb && dpkg -i /tmp/pure-ftpd-mysql/pure-ftpd-mysql*.deb
# Prevent pure-ftpd upgrading
RUN apt-mark hold pure-ftpd-common pure-ftpd-mysql
# setup ftpgroup and ftpuser
RUN groupadd ftpgroup && useradd -g ftpgroup -d /dev/null -s /etc ftpuser
RUN apt-get -qq update && apt-get -y -qq install quota quotatool

# Install BIND DNS Server
RUN apt-get -y install bind9 dnsutils haveged

# Install Vlogger, Webalizer, And AWStats
RUN apt-get -y install vlogger webalizer awstats geoip-database libclass-dbi-mysql-perl libtimedate-perl
ADD etc/cron.d/awstats /etc/cron.d/

# Install Jailkit
RUN apt-get -y install build-essential autoconf automake libtool flex bison debhelper binutils
RUN cd /tmp \
&& wget https://olivier.sessink.nl/jailkit/jailkit-2.20.tar.gz \
&& tar xvfz jailkit-2.20.tar.gz \
&& cd jailkit-2.20 \
&& echo 5 > debian/compat \
&& ./debian/rules binary \
&& cd /tmp \
&& dpkg -i jailkit_2.20-1_*.deb \
&& rm -rf jailkit-2.20*

# Install fail2ban
RUN apt-get -y install fail2ban
ADD ./etc/fail2ban/jail.local /etc/fail2ban/jail.local
ADD ./etc/fail2ban/filter.d/pureftpd.conf /etc/fail2ban/filter.d/pureftpd.conf
ADD ./etc/fail2ban/filter.d/dovecot-pop3imap.conf /etc/fail2ban/filter.d/dovecot-pop3imap.conf
RUN echo "ignoreregex =" >> /etc/fail2ban/filter.d/postfix-sasl.conf
RUN service fail2ban restart

# Install RoundCube
RUN service mysql start && apt-get -y install roundcube roundcube-core roundcube-mysql roundcube-plugins
ADD ./etc/apache2/conf-enabled/roundcube.conf /etc/apache2/conf-enabled/roundcube.conf
ADD ./etc/roundcube/config.inc.php /etc/roundcube/config.inc.php
RUN service apache2 restart

# Install ISPConfig 3
RUN cd /root && wget http://www.ispconfig.org/downloads/ISPConfig-3-stable.tar.gz && tar xfz ISPConfig-3-stable.tar.gz

ADD ./etc/clamav/clamd.conf /etc/clamav/clamd.conf

RUN echo "export TERM=xterm" >> /root/.bashrc

# ISPConfig initialization and startup script
ADD ./start.sh /start.sh
ADD ./supervisord.conf /etc/supervisor/supervisord.conf
ADD ./etc/cron.daily/sql_backup.sh /etc/cron.daily/sql_backup.sh
ADD ./autoinstall.ini /root/ispconfig3_install/install/autoinstall.ini
RUN mkdir -p /var/run/sshd /var/log/supervisor /var/run/supervisor
RUN mv /bin/systemctl /bin/systemctloriginal
ADD ./bin/systemctl /bin/systemctl
RUN chmod 755 /start.sh /bin/systemctl

RUN mkdir -p /var/backup/sql
RUN freshclam

EXPOSE 20/tcp 21/tcp 22/tcp 53 953/tcp 8080/tcp 30000 30001 30002 30003 30004 30005 30006 30007 30008 30009 3306

# CLEANING
RUN apt-get autoremove -y && apt-get clean && rm -rf /tmp/*

VOLUME ["/var/www/","/var/mail/","/var/backup/","/var/lib/mysql","/var/log/"]

CMD ["/bin/bash", "/start.sh"]
