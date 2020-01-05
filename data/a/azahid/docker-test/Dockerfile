FROM odoo:10

USER root

RUN set -x; \
        curl -o odoo.deb -SL http://nightly.odoo.com/10.0/nightly/deb/odoo_10.0.latest_all.deb \
        && dpkg --force-depends -i odoo.deb \
        && rm odoo.deb

RUN apt-get update
RUN python -m pip install -U pip
RUN apt-get install -y build-essential libssl-dev libffi-dev python-dev
RUN apt-get install -y libpq-dev python-dev libxml2-dev libxslt1-dev libldap2-dev libsasl2-dev libffi-dev
RUN pip install pysftp==0.2.8


USER odoo
