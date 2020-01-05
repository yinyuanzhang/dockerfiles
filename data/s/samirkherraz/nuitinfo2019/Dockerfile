from dotriver/ubuntu-s6

RUN set -x \
    && apt update \
    && apt install -y nginx python3 make \
    && apt autoclean \
    && apt clean \
    && mkdir /data/ \
    && rm -R /var/www/* || true

ADD etc  /etc
ADD nuitdelinfo /data/nuitdelinfo
ADD static  /data/static
ADD uploads  /data/uploads
ADD Makefile  /data/
ADD manage.py  /data/


RUN set -x \
    && cd /data \
    && apt update \
    && make install \
    && apt autoclean \
    && apt clean


RUN set -x \
    && chmod +x /etc/cont-init.d/* \
    && chmod +x /etc/s6/services/*/*
