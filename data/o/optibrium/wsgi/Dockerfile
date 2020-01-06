FROM debian:buster

COPY default.conf /etc/apache2/sites-enabled/000-default.conf

RUN apt update \
    && apt install -y \
        apache2 \
        python3.7 \
        python3-pip \
        python3-dev \
        python3-setuptools \
        libapache2-mod-wsgi-py3

CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]
