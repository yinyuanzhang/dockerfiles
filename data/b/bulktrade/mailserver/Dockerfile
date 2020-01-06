FROM ubuntu:14.04
MAINTAINER Thomas VIAL

# Packages
RUN apt-get update -q --fix-missing
RUN apt-get -y upgrade
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install vim postfix sasl2-bin courier-imap courier-imap-ssl \
    courier-pop courier-pop-ssl courier-authdaemon supervisor gamin amavisd-new spamassassin clamav clamav-daemon libnet-dns-perl libmail-spf-perl \
    pyzor razor arj bzip2 cabextract cpio file gzip nomarch p7zip pax unzip zip zoo rsyslog mailutils netcat \
    opendkim opendkim-tools opendmarc curl fail2ban
RUN apt-get autoclean && rm -rf /var/lib/apt/lists/*

# Configures Saslauthd
RUN rm -rf /var/run/saslauthd && ln -s /var/spool/postfix/var/run/saslauthd /var/run/saslauthd
RUN adduser postfix sasl
RUN echo 'NAME="saslauthd"\nSTART=yes\nMECHANISMS="sasldb"\nTHREADS=0\nPWDIR=/var/spool/postfix/var/run/saslauthd\nPIDFILE="${PWDIR}/saslauthd.pid"\nOPTIONS="-n 0 -c -m /var/spool/postfix/var/run/saslauthd"' > /etc/default/saslauthd

# Configures Courier
RUN sed -i -r 's/daemons=5/daemons=1/g' /etc/courier/authdaemonrc
RUN sed -i -r 's/authmodulelist="authpam"/authmodulelist="authuserdb"/g' /etc/courier/authdaemonrc

# Enables Spamassassin and CRON updates
RUN sed -i -r 's/^(CRON|ENABLED)=0/\1=1/g' /etc/default/spamassassin

# Enables Amavis
RUN sed -i -r 's/#(@|   \\%)bypass/\1bypass/g' /etc/amavis/conf.d/15-content_filter_mode
RUN adduser clamav amavis
RUN adduser amavis clamav
RUN useradd -u 5000 -d /home/docker -s /bin/bash -p $(echo docker | openssl passwd -1 -stdin) docker

# Enables Clamav
RUN chmod 644 /etc/clamav/freshclam.conf
RUN (crontab -l ; echo "0 1 * * * /usr/bin/freshclam --quiet") | sort - | uniq - | crontab -
RUN freshclam

# Configure DKIM (opendkim)
RUN mkdir -p /etc/opendkim/keys
ADD postfix/TrustedHosts /etc/opendkim/TrustedHosts
# DKIM config files
ADD postfix/opendkim.conf /etc/opendkim.conf
ADD postfix/default-opendkim /etc/default/opendkim

# Configure DMARC (opendmarc)
ADD postfix/opendmarc.conf /etc/opendmarc.conf
ADD postfix/default-opendmarc /etc/default/opendmarc

# Configures Postfix
ADD postfix/main.cf /etc/postfix/main.cf
ADD postfix/master.cf /etc/postfix/master.cf
ADD postfix/sasl/smtpd.conf /etc/postfix/sasl/smtpd.conf
ADD bin/generate-ssl-certificate /usr/local/bin/generate-ssl-certificate
RUN chmod +x /usr/local/bin/generate-ssl-certificate

# Get LetsEncrypt signed certificate
RUN curl https://letsencrypt.org/certs/lets-encrypt-x1-cross-signed.pem > /etc/ssl/certs/lets-encrypt-x1-cross-signed.pem
RUN curl https://letsencrypt.org/certs/lets-encrypt-x2-cross-signed.pem > /etc/ssl/certs/lets-encrypt-x2-cross-signed.pem

# Start-mailserver script
ADD start-mailserver.sh /usr/local/bin/start-mailserver.sh
RUN chmod +x /usr/local/bin/start-mailserver.sh

# SMTP ports
EXPOSE  25
EXPOSE  587

# IMAP ports
EXPOSE  143
EXPOSE  993

# POP3 ports
EXPOSE  110
EXPOSE  995

CMD /usr/local/bin/start-mailserver.sh
