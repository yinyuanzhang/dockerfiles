FROM debian:stretch
MAINTAINER Jesus Zapata <chuchocorleone@gmail.com>

# utf-8 encoding
ENV LANG C.UTF-8

# Install some deps, lessc and less-plugin-clean-css, and wkhtmltopdf
RUN set -x; \
        apt-get update \
        && apt-get install -y --no-install-recommends \
            ca-certificates \
            curl \
            nodejs \
            node-less \
            python3 \
            python3-gevent \
            python3-pip \
            python3-renderpm \
            python3-watchdog \
            python3-pdfkit \
            wkhtmltopdf \
            gnupg2 \
        && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false -o APT::AutoRemove::SuggestsImportant=false

# Install nodejs
RUN curl -sL https://deb.nodesource.com/setup_4.x | bash - \
        && apt-get install -y --no-install-recommends nodejs \
        && npm install -g less less-plugin-clean-css

# Install pip3 packages
RUN pip3 install setuptools wheel \
        && pip3 install num2words wizard

# Install Odoo
ENV ODOO_VERSION 11.0
ENV ODOO_RELEASE 20171004
RUN set -x; \
        curl -o odoo.deb -SL http://nightly.odoo.com/${ODOO_VERSION}/nightly/deb/odoo_${ODOO_VERSION}.${ODOO_RELEASE}_all.deb \
        && echo '2037f9d2a0d8ce2a1797ebed71fa809a6a8ef8d4 odoo.deb' | sha1sum -c - \
        && apt-get -y --fix-broken install ./odoo.deb \
        && apt-get update \
        && apt-get -y install -f --no-install-recommends \
        && rm -rf /var/lib/apt/lists/* odoo.deb

# Copy entrypoint script and Odoo configuration file
COPY ./entrypoint.sh /
COPY ./odoo.conf /etc/odoo/
RUN chown odoo /etc/odoo/odoo.conf

# Mount /var/lib/odoo to allow restoring filestore and /mnt/extra-addons for users addons
RUN mkdir -p /mnt/addons \
        && chown -R odoo /mnt/addons
RUN mkdir -p /mnt/extra-addons \
        && chown -R odoo /mnt/extra-addons
VOLUME ["/var/lib/odoo", "/mnt/addons", "/mnt/extra-addons"]

# Expose Odoo services
EXPOSE 8069 8071

# Set the default config file
ENV ODOO_RC /etc/odoo/odoo.conf

# Set default user when running the container
USER odoo

ENTRYPOINT ["/entrypoint.sh"]
CMD ["odoo"]
