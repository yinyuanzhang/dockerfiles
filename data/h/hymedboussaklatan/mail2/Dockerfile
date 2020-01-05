FROM ubuntu:latest

RUN apt-get -y update
RUN apt-get -y upgrade
RUN apt-get install -y rsyslog
RUN apt-get install -y postfix
RUN apt-get install -y dovecot-common
RUN apt-get install -y dovecot-imapd
RUN apt-get install -y dovecot-pop3d
RUN apt-get install -y mailutils
RUN apt-get install -y vim

COPY mail2/postfix/master.cf /etc/postfix/master.cf
COPY mail2/postfix/main.cf /etc/postfix/main.cf
COPY mail2/postfix/aliases /etc/aliases

COPY mail2/dovecot/dovecot.conf /etc/dovecot/dovecot.conf
COPY mail2/dovecot/10-master.conf /etc/dovecot/conf.d/10-master.conf
COPY mail2/dovecot/10-auth.conf /etc/dovecot/conf.d/10-auth.conf
COPY mail2/dovecot/10-mail.conf /etc/dovecot/conf.d/10-mail.conf


COPY mail2/start.sh /start.sh
RUN chmod -R 777 /start.sh

RUN postalias /etc/aliases

VOLUME ["/var/mail","/home/201525"]

#SMTP
EXPOSE 25
#unfitlered SMTP
EXPOSE 2525
#this is the default IMAP non-encrypted port
EXPOSE 143
#This is the default mail submission port
EXPOSE 587
#IMAP securely
EXPOSE 993

CMD ["sh", "-c", "/start.sh"]
