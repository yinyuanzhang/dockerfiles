FROM pushtospace/postfix-dovecot-mysql

MAINTAINER Gino Jongenelen <gino@daza.nl>

ADD main.cf /etc/postfix/
ADD sasl_passwd /etc/postfix/
ADD transport /etc/postfix/
ADD mysql-virtual-vacation.cf /etc/postfix/
ADD transport /etc/postfix/
RUN postmap /etc/postfix/sasl_passwd && postmap /etc/postfix/transport
ADD dovecot.conf /etc/dovecot/
ADD ./start.sh /root

RUN chmod +x /root/start.sh