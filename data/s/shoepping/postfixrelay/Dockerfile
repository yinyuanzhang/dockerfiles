FROM debian:stretch-slim

# install default packages
run echo "postfix postfix/main_mailer_type string 'Internet site'" > postinstallconf.txt
run echo "postfix postfix/mailname string mail.shoeppingtest.at" >> postinstallconf.txt
run debconf-set-selections postinstallconf.txt
run DEBIAN_FRONTEND=noninteractive
run apt-get update && \
    apt-get -y --no-install-recommends install \
    apache2 \
    bash \
    ca-certificates \
    curl \
    libsasl2-modules \
    mailutils \
    nano \
    postfix \
    procps \
    rsyslog \
    sed \
    tar \
    wget && \
    rm -rf /var/cache/apk/* && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

COPY rsyslog.conf /etc/rsyslog.conf
COPY run /root/
RUN chmod +x /root/run
# VOLUME ["/var/lib/postfix", "/var/mail", "/var/spool/postfix"]
EXPOSE 25
CMD ["/root/run"]
