FROM ubuntu:latest
LABEL build="201910161645"
LABEL maintainer "marc.jakob@bs.ch"

COPY dpkg-excludes /etc/dpkg/dpkg.cfg.d/excludes
COPY start.sh /

RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-selections && \
    apt-get update && \
    apt-get -y install locales gnupg wget && \
    locale-gen en_US.UTF-8 && \
    locale-gen de_CH.UTF-8 && \
        locale-gen de_DE.UTF-8 && \
        update-locale && \
    echo "deb http://packages.icinga.org/ubuntu icinga-bionic main" >> /etc/apt/sources.list.d/icinga.list && \
    echo "deb-src http://packages.icinga.org/ubuntu icinga-bionic main" >> /etc/apt/sources.list.d/icinga.list && \
    apt-key adv --fetch-keys http://packages.icinga.org/icinga.key && \
    apt-get update && \
    apt-get -y install postgresql apache2 && \
    rm -r /var/lib/postgresql/10/main && \
    mkdir -p /var/lib/postgresql/10/main && \
    chown postgres /var/lib/postgresql/10/main && \
    su - postgres -c "/usr/lib/postgresql/10/bin/initdb -D /var/lib/postgresql/10/main -E UTF8 --locale=de_CH.utf8"

COPY pg_hba.conf /var/lib/postgresql/10/main/

RUN chown postgres:postgres /var/lib/postgresql/10/main/pg_hba.conf && \
        chmod 0640 /var/lib/postgresql/10/main/pg_hba.conf && \
        su - postgres -c "/usr/lib/postgresql/10/bin/pg_ctl -D /var/lib/postgresql/10/main -l logfile start" && \
        apt-get install icinga2 nagios-plugins libapache2-mod-auth-kerb libapache2-mod-auth-openidc icingaweb2 libapache2-mod-php php \
        php-pgsql php-gd icinga2-ido-pgsql postfix bsd-mailx -y && \
        apt-get --no-install-recommends install nagios-nrpe-plugin -y && \
        wget -O /usr/lib/nagios/plugins/check_elasticsearch https://raw.githubusercontent.com/orthecreedence/check_elasticsearch/master/check_elasticsearch && \
        chmod 0755 /usr/lib/nagios/plugins/check_elasticsearch && \
        apt-get clean && \
        tar -cf /cfg.tar /var/www /etc/apache2 /etc/icinga2 /etc/icingaweb2 /var/lib/postgresql && \
        rm -rf           /var/www /etc/apache2 /etc/icinga2 /etc/icingaweb2 /var/lib/postgresql /var/lib/apt/lists/* && \
        chmod 0750 /start.sh

EXPOSE 80
VOLUME  ["/var/www", "/etc/apache2", "/var/log/apache2", "/etc/icinga2", "/etc/icingaweb2", "/var/lib/postgresql" ]
ENTRYPOINT ["/start.sh"]
