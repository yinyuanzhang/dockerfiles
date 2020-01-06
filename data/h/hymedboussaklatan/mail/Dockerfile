FROM ubuntu:latest
RUN apt update -y && apt upgrade -y

RUN touch /var/log/tallylog
RUN chmod 600 /var/log/tallylog

RUN apt install nano -y && DEBIAN_FRONTEND=noninteractive apt install postfix -y
RUN DEBIAN_FRONTEND=noninteractive apt install dovecot-core dovecot-imapd dovecot-pop3d dovecot-lmtpd -y
RUN apt install dovecot-sieve dovecot-managesieved -y

RUN mkdir /var/mail/vhosts
RUN mkdir /var/mail/vhosts/wt12.ephec-ti.be
RUN groupadd -g 5000 vmail
RUN useradd -r -g vmail -u 5000 vmail -d /var/mail/vhosts -c "virtual mail user"
RUN chown -R vmail:vmail /var/mail/vhosts/


COPY mail/hosts /etc/hosts
COPY mail/mailname /etc/mailname

COPY mail/postfix/main.cf /etc/postfix/main.cf
COPY mail/postfix/virtual_mailbox_domains /etc/postfix/virtual_mailbox_domains
#COPY mail/postfix/virtual_alias /etc/postfix/virtual_alias
COPY mail/postfix/master.cf /etc/postfix/master.cf

COPY mail/dovecot/10-mail.conf /etc/dovecot/conf.d/10-mail.conf
COPY mail/dovecot/10-master.conf /etc/dovecot/conf.d/10-master.conf
COPY mail/dovecot/10-auth.conf /etc/dovecot/conf.d/10-auth.conf
#COPY mail/dovecot/10-ssl.conf /etc/dovecot/conf.d/10-ssl.conf
COPY mail/dovecot/auth-passwdfile.conf.ext /etc/dovecot/conf.d/auth-passwdfile.conf.ext
COPY mail/dovecot/dovecot-users /etc/dovecot/dovecot-users
COPY mail/start_services.sh /tools/start_services.sh

RUN postmap /etc/postfix/virtual_mailbox_domains
#RUN postmap /etc/postfix/virtual_alias



EXPOSE 25 110 143 465 587 993 995


