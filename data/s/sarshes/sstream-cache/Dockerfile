FROM ubuntu:18.04

RUN apt -qq update && \
    apt install -y simplestreams apache2 \
    gpgv ubuntu-cloudimage-keyring \
    python-certifi --no-install-recommends file && \
    apt clean all

RUN sstream-mirror --keyring=/usr/share/keyrings/ubuntu-cloudimage-keyring.gpg \
    https://images.maas.io/ephemeral-v3/daily/ \
    /var/www/html/maas/images/ephemeral-v3/daily 'os~(grub*|pxelinux)' --max=1 --progress

RUN sstream-mirror --keyring=/usr/share/keyrings/ubuntu-cloudimage-keyring.gpg \
    https://images.maas.io/ephemeral-v3/daily/ \
    /var/www/html/maas/images/ephemeral-v3/daily \
    'arch=amd64' 'release~bionic' --max=1 --progress

RUN sh -c 'echo "" > /etc/apache2/ports.conf'

ENV APACHE_RUN_USER www-data
ENV APACHE_RUN_GROUP www-data
ENV APACHE_PID_FILE /var/run/apache2.pid
ENV APACHE_RUN_DIR /var/run/
ENV APACHE_LOCK_DIR /var/lock
ENV APACHE_LOG_DIR /var/log/
ENV LANG C

ENTRYPOINT ["/usr/sbin/apache2"]
CMD ["-E", "/dev/stderr","-c","ErrorLog /dev/stderr","-c","Listen 8888","-c","ServerRoot /etc/apache2","-c","DocumentRoot /var/www/html","-D","FOREGROUND"]
