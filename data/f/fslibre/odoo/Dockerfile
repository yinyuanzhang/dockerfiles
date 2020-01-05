FROM odoo:12.0
MAINTAINER Odoo S.A. <info@odoo.com>

USER root

RUN set -x; \
        apt-get update \
        && apt-get install -y --no-install-recommends \
            git \
            vim \
            mc \
            python3-dev \
            python3-pandas \
            default-jdk \
            default-jre \
            libreoffice-writer \
            libreoffice-calc

RUN pip3 install \
        pyotp \
        unidecode \
        wand \
        checksumdir \
        cachetools \
        validate_email \
        simplejson \
        oauthlib \
        pyqrcode \ 
        pyldap \
        zeep \
        xmltodict \
        odoorpc \
        openpyxl \
        pyzk \
        viivakoodi \
        raven \
        xlrd \
        xlwt \
        email_validator \
        py3o.template \
        py3o.formats \
        PyPDF2

RUN python3 -m pip install redis
RUN python3 -m pip install paramiko
RUN pip3 install git+git://github.com/OCA/openupgradelib.git

RUN usermod -u 1500 odoo
RUN groupmod -g 1500 odoo

USER odoo
