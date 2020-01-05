FROM debian:jessie
RUN useradd -G sudo -p $(perl -e'print crypt("tester", "tester")') -m -s /bin/bash -N tester \
    && apt-get update \
    && echo "postfix postfix/mailname string develop.dev" | debconf-set-selections \
    && echo "postfix postfix/main_mailer_type select Local only" | debconf-set-selections \
    && DEBIAN_FRONTEND=noninteractive apt-get -y install postfix dovecot-imapd supervisor \
    && postconf -e "home_mailbox = Maildir/" \
    && postconf -e "mailbox_command =" \
    && postconf -e "inet_interfaces = all" \
    && sed -i 's@mail_location = mbox:~/mail:INBOX=/var/mail/%u@mail_location = maildir:~/Maildir@' /etc/dovecot/conf.d/10-mail.conf \
    && sed -i 's@#disable_plaintext_auth = yes@disable_plaintext_auth = no@' /etc/dovecot/conf.d/10-auth.conf \
    && maildirmake.dovecot /etc/skel/Maildir \
    && maildirmake.dovecot /etc/skel/Maildir/.Archive \
    && cp -r /etc/skel/Maildir /home/tester \
    && chown -R tester /home/tester/Maildir \
    && chmod 700 /home/tester/Maildir \
    && echo "[supervisord]" > /etc/supervisor/conf.d/supervisord.conf \
    && echo "nodaemon=true" >> /etc/supervisor/conf.d/supervisord.conf \
    && echo "[program:postfix]" >> /etc/supervisor/conf.d/supervisord.conf \
    && echo "process_name=master" >> /etc/supervisor/conf.d/supervisord.conf \
    && echo "directory=/etc/postfix" >> /etc/supervisor/conf.d/supervisord.conf \
    && echo "command=/usr/sbin/postfix -c /etc/postfix start" >> /etc/supervisor/conf.d/supervisord.conf \
    && echo "startsecs=0" >> /etc/supervisor/conf.d/supervisord.conf \
    && echo "autorestart=false" >> /etc/supervisor/conf.d/supervisord.conf \
    && echo "[program:dovecot]" >> /etc/supervisor/conf.d/supervisord.conf \
    && echo "command=/usr/sbin/dovecot -c /etc/dovecot/dovecot.conf -F" >> /etc/supervisor/conf.d/supervisord.conf \
    && echo "autorestart=true" >> /etc/supervisor/conf.d/supervisord.conf
EXPOSE 25 143 993
CMD ["/usr/bin/supervisord"]