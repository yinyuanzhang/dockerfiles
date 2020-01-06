FROM debian:stretch

MAINTAINER Gabriel Juelke <pyriand3r@gmail.com> 

ENV RESTYABOARD_VERSION 0.6.7

RUN echo "postfix postfix/mailname string localhost" | debconf-set-selections && \ 
    echo "postfix postfix/main_mailer_type string 'Internet Site'" | debconf-set-selections && \
    apt-get update && \
    apt-get install -y --no-install-recommends \ 
        ca-certificates \ 
        cron \ 
        curl \ 
        nginx \ 
        php7.0-curl \
        php7.0-fpm \ 
        php7.0-geoip \ 
        php7.0-imagick \ 
        php7.0-imap \ 
        php7.0-ldap \ 
        php7.0-pgsql \ 
        postfix \ 
        postgresql-client \ 
        unzip \ 
        && \ 
        rm -rf /var/lib/apt/lists/* 
        
# download and install restyaboard
RUN curl -L -o /tmp/restyaboard.zip https://github.com/RestyaPlatform/board/releases/download/v${RESTYABOARD_VERSION}/board-v${RESTYABOARD_VERSION}.zip && \ 
    unzip /tmp/restyaboard.zip -d /usr/share/nginx/html && \
    rm /tmp/restyaboard.zip && \
    cp /usr/share/nginx/html/restyaboard.conf /etc/nginx/sites-enabled/default && \ 
    mkdir -p /etc/restyaboard && \
    mv /usr/share/nginx/html/server/php/config.inc.php /usr/share/nginx/html/server/php/config.inc.php.back

# set permissions
RUN chmod 755 /usr/share/nginx/html/server/php/shell/*.sh && \
    chmod -R 755 /usr/share/nginx/html/media && \
    chmod -R 755 /usr/share/nginx/html/client && \
    chmod -R 755 /usr/share/nginx/html/tmp/cache && \
    chmod -R 755 /usr/share/nginx/html/server

# set up cronjobs
RUN { \
		echo '* * * * * /usr/share/nginx/htmlserver/php/shell/indexing_to_elasticsearch.sh'; \
		echo '* * * * * /usr/share/nginx/htmlserver/php/shell/instant_email_notification.sh'; \
		echo '0 * * * * /usr/share/nginx/htmlserver/php/shell/periodic_email_notification.sh'; \
		echo '* * * * * /usr/share/nginx/htmlserver/php/shell/imap.sh'; \
		echo '* * * * * /usr/share/nginx/htmlserver/php/shell/webhook.sh'; \
		echo '* * * * * /usr/share/nginx/htmlserver/php/shell/card_due_notification.sh'; \
	} > /var/spool/cron/crontabs/root

COPY run.sh /usr/local/bin

VOLUME /etc/restyaboard /usr/share/nginx/html/media

WORKDIR /usr/share/nginx/html

EXPOSE 80

CMD ["run.sh"]
