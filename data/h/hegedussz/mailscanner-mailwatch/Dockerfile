FROM debian:8.10

MAINTAINER Szabolcs Hegedus <szabolcs.hegedus@gmail.com>

ENV MAILSCAN_VERSION 5.0.6-5


RUN apt-get update && apt-get install --no-install-recommends --yes \
    runit \
    apache2 \
    ca-certificates \
    libapache2-mod-fcgid \
    git \
    wget \
    curl \
    mc \
    nload \
    htop \
    exim4 \
    libmysqlclient-dev \
    php5 \
    php5-mysqlnd \
    nano \
    && rm -rf /var/lib/apt/lists/* \
    && rm -rf /usr/share/doc/* \
    && rm -rf /var/cache/debconf/*

RUN mkdir /home/mailscanner
RUN curl -o /home/mailscanner/MailScanner-$MAILSCAN_VERSION.deb.tar.gz  -L https://s3.amazonaws.com/msv5/release/MailScanner-$MAILSCAN_VERSION.deb.tar.gz \
    && cd /home/mailscanner && tar -xf /home/mailscanner/MailScanner-5.0.6-5.deb.tar.gz \
    && cd /home/mailscanner/MailScanner-5.0.6-5 && chmod 755 install.sh && ./install.sh --MTA=none --ignoreDeps=N

RUN cpan cpan -i DBD::mysql
RUN cpan -i Encoding::FixLatin && cpan -i Digest::SHA1

RUN mkdir /opt/mailwatch
RUN cd /opt/mailwatch \ && git clone --depth=1 https://github.com/mailwatch/MailWatch.git .
RUN  ln -s /opt/mailwatch/MailScanner_perl_scripts/MailWatch.pm /usr/share/MailScanner/perl/custom \
    && ln -s /opt/mailwatch/MailScanner_perl_scripts/SQLBlackWhiteList.pm /usr/share/MailScanner/perl/custom \
    && ln -s /opt/mailwatch/MailScanner_perl_scripts/SQLSpamSettings.pm /usr/share/MailScanner/perl/custom \
    && cp /opt/mailwatch/MailScanner_perl_scripts/MailWatchConf.pm /usr/share/MailScanner/perl/custom/MailWatchConf.pm \
    && cp /opt/mailwatch/mailscanner/lib/pear/PEAR.php /opt/mailwatch/mailscanner/lib/pear/Mail/PEAR.php


RUN rm -rf /home

COPY docker/ /

RUN a2enmod rewrite expires && \
    chown -R www-data:www-data /opt/mailwatch/mailscanner /var/www/fastcgidefs/php.wrapper && \
    chmod 755 -R /var/www/fastcgidefs/* /etc/service/*/run
RUN chown -R clamav:clamav /var/run/clamav/
RUN chmod 755 -R /var/run/clamav/*
RUN apt-get install SpamAssassin --yes
RUN sa-update && spamassassin -D -p /etc/MailScanner/spamassassin.conf --lint


RUN mkdir /etc/cron.daily/mailwatch
# Database cleanup of maillog records
RUN cp -R /opt/mailwatch/tools/Cron_jobs /etc/cron.daily/ && chmod +x /etc/cron.daily/mailwatch
RUN cp /opt/mailwatch/tools/Cron_jobs/mailwatch_db_clean.php /usr/local/bin/ && chmod +x /usr/local/bin/mailwatch_db_clean.php
# Quarantine Maintenance
RUN cp /opt/mailwatch/tools/Cron_jobs/mailwatch_quarantine_maint.php /usr/local/bin/ && chmod +x /usr/local/bin/mailwatch_quarantine_maint.php
# Quarantine Reporting
RUN cp /opt/mailwatch/tools/Cron_jobs/mailwatch_quarantine_report.php /usr/local/bin/ && chmod +x /usr/local/bin/mailwatch_quarantine_report.php


RUN php /opt/mailwatch/upgrade.php --skip-user-confirm /opt/mailwatch/mailscanner/functions.php

# Start runit service
ENTRYPOINT ["/usr/bin/runsvdir", "-P", "/etc/service"]


EXPOSE 80
