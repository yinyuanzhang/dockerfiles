FROM adhoc/odoo-adhoc:8.0
MAINTAINER Juan Jose Scarafia <jjs@adhoc.com.ar>

USER root

# Install dependencies
RUN apt-get update -qq
RUN apt-get install -y supervisor postgresql \
                       postgresql-server-dev-9.4 postgresql-client \
                       postgresql-contrib-9.4

# Install aeroo docs
RUN DEBIAN_FRONTEND=noninteractive && \
    apt-get install -y python3-uno libreoffice-writer libreoffice-calc python3-pip xvfb openjdk-7-jre && \
    apt-get clean
RUN pip3 install jsonrpc2
RUN pip3 install daemonize
RUN git clone https://github.com/aeroo/aeroo_docs.git /opt/aeroo_docs

# Fix AUFL issue regarding permissions
RUN mv /etc/ssl/private /etc/ssl/private-2
RUN mv /etc/ssl/private-2 /etc/ssl/private

## Clean apt-get (copied from odoo)
RUN apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false -o APT::AutoRemove::SuggestsImportant=false
RUN apt-get clean
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

USER postgres

# Prepare database
RUN service postgresql start && createuser --superuser --createdb --username postgres --no-createrole -w odoo
RUN service postgresql start && createdb -O odoo odoo

USER root

# Run
ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf
CMD supervisord -c /etc/supervisor/conf.d/supervisord.conf
