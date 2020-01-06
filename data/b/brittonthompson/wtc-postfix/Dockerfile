FROM ubuntu:latest

RUN apt-get update
#RUN debconf-set-selections preseed.txt
RUN DEBIAN_FRONTEND=noninteractive apt-get install -q -y postfix

RUN postconf -e myhostname=smtp.websitetotalcare.com
RUN postconf -e mydestination=
RUN postconf -e local_recipient_maps=
RUN postconf -e mynetworks=cidr:/etc/postfix/mynetworks
RUN postconf -e relayhost=relay.websitetotalcare.com:2525
RUN postconf -e smtpd_relay_restrictions=permit_mynetworks,permit_sasl_authenticated,defer_unauth_destination
RUN postconf -e smtpd_tls_cert_file=/etc/ssl/certs/ssl-cert-snakeoil.pem
RUN postconf -e smtpd_tls_key_file=/etc/ssl/private/ssl-cert-snakeoil.key
RUN postconf -e smtpd_use_tls=yes
RUN postconf -e smtpd_tls_session_cache_database=btree:${data_directory}/smtpd_scache
RUN postconf -e smtp_tls_session_cache_database=btree:${data_directory}/smtp_scache

ADD mynetworks /etc/postfix/mynetworks
ADD mailname /etc/mailname

# Use syslog-ng to get Postfix logs
RUN apt-get install -q -y syslog-ng

EXPOSE 25

#service syslog-ng start ; 
CMD ["sh", "-c", "service syslog-ng start ; service postfix start ; tail -F /var/log/mail.log"] 
