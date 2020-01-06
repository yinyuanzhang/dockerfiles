FROM python:3.7-slim-buster AS base

# Enable Odoo user and filestore
RUN useradd -md /home/odoo -s /bin/false odoo \
    && mkdir -p /var/lib/odoo \
    && chown -R odoo:odoo /var/lib/odoo \
    && sync

# VOLUME ["/var/lib/odoo"]
EXPOSE 8069 8072

# create directory for default and custom odoo files - ADHOC
# directories to be mounted (to be persisted)
ENV DATA_DIR /opt/odoo/odoo_data
ENV CUSTOM_ADDONS /opt/odoo/custom/repositories
ENV ODOO_UPGRADE_PATH /opt/odoo/default/odoo-upgrade
# Other directories for odoo files (no to be persited)
ENV ETC_DIR /opt/odoo/default/etc
ENV EXTRA_ADDONS /opt/odoo/default/repositories
ENV RESOURCES /opt/odoo/default/resources
RUN mkdir -p ${ETC_DIR} && \
    mkdir -p ${DATA_DIR} && \
    mkdir -p ${EXTRA_ADDONS} && \
    mkdir -p ${CUSTOM_ADDONS} && \
    mkdir -p ${RESOURCES} && \
    chown -R odoo.odoo /opt/odoo && \
    sync

# replace entrypoint script and replace Odoo configuration file - ADHOC
COPY ./resources/ ${RESOURCES}/
COPY ./resources/.vimrc ~/.vimrc

# change entrypoint - ADHOC
ENTRYPOINT ["/opt/odoo/default/resources/entrypoint.sh"]
CMD ["odoo"]

# Variables used by the launch scripts - ADHOC
ENV \
    ODOO_SERVER=odoo \
    ODOO_CONF=/opt/odoo/default/etc/odoo.conf \
    FIXDBS=False \
    WAIT_PG=True \
    # odoo conf variables
    DB_MAXCONN=64 \
    MAX_CRON_THREADS=1 \
    SMTP_SERVER=localhost \
    SMTP_PORT=25 \
    SMTP_SSL=False \
    SMTP_USER=False \
    SMTP_PASSWORD=False \
    UNACCENT=True \
    PGUSER=odoo \
    PGPASSWORD=odoo \
    PGHOST=db \
    PGPORT=5432 \
    WORKERS=6 \
    ADMIN_PASSWORD=admin \
    SERVER_MODE=test \
    DISABLE_SESSION_GC=false \
    FILESTORE_OPERATIONS_THREADS=3 \
    FILESTORE_COPY_HARD_LINK=True \
    PROXY_MODE=True \
    WITHOUT_DEMO=True \
    DBFILTER=.* \
    LIST_DB=False \
    LIMIT_TIME_CPU=600 \
    LIMIT_TIME_REAL=1200 \
    LIMIT_TIME_REAL_CRON=1200 \
    LIMIT_MEMORY_HARD=2684354560 \
    LIMIT_MEMORY_SOFT=2147483648 \
    AEROO_DOCS_HOST=aeroo \
    AFIP_HOMO_PKEY_FILE=/opt/odoo/backups/homo.pkey \
    AFIP_HOMO_CERT_FILE=/opt/odoo/backups/homo.cert \
    AFIP_PROD_PKEY_FILE=/opt/odoo/backups/prod.pkey \
    AFIP_PROD_CERT_FILE=/opt/odoo/backups/prod.cert \
    ENABLE_REDIS=False \
    REDIS_HOST=localhost \
    REDIS_PORT=6379 \
    REDIS_DBINDEX=1 \
    REDIS_PASS=False \
    DB_TEMPLATE=template1

# odoo server use this env var as default conf, check if v9 or v10 rename it - ADHOC
ENV ODOO_RC $ODOO_CONF

ARG WKHTMLTOPDF_VERSION=0.12.5
ARG WKHTMLTOPDF_CHECKSUM='1140b0ab02aa6e17346af2f14ed0de807376de475ba90e1db3975f112fbd20bb'
ENV LC_ALL=C.UTF-8 \
    NODE_PATH=/usr/local/lib/node_modules:/usr/lib/node_modules
     #\PATH="/home/odoo/.local/bin:$PATH"

# Other requirements and recommendations to run Odoo
# See https://github.com/$ODOO_SOURCE/blob/$ODOO_VERSION/debian/control
RUN apt-get -qq update \
    && apt-get -yqq upgrade \
    && apt-get install -yqq --no-install-recommends \
        chromium \
        ffmpeg \
        python3 \
        fontconfig libfreetype6 libxml2 libxslt1.1 libjpeg62-turbo zlib1g \
        libfreetype6  libtiff5 \
        libx11-6 libxext6 libxrender1 \
        locales-all zlibc \
        bzip2 ca-certificates curl fonts-liberation2 gettext-base git nano \
        postgresql-client telnet xz-utils \
        # agregado - ADHOC
        node-less node-clean-css \
        # a pedido de kat
        vim vim-athena vim-syntastic vim-pathogen tmux \
    && curl https://bootstrap.pypa.io/get-pip.py | python3 /dev/stdin --no-cache-dir \
    # && curl -sL https://deb.nodesource.com/setup_6.x | bash - \
    # && apt-get install -yqq nodejs \
    && curl -SLo wkhtmltox.deb https://github.com/wkhtmltopdf/wkhtmltopdf/releases/download/${WKHTMLTOPDF_VERSION}/wkhtmltox_${WKHTMLTOPDF_VERSION}-1.stretch_amd64.deb \
    && echo "${WKHTMLTOPDF_CHECKSUM}  wkhtmltox.deb" | sha256sum -c - \
    && apt-get install -yqq --no-install-recommends ./wkhtmltox.deb \
    && rm wkhtmltox.deb \
    && wkhtmltopdf --version \
    && apt-get -yqq purge python2.7 \
    && apt-get -yqq autoremove \
    && rm -Rf /var/lib/apt/lists/*
# sacamos para liberar espacio y porque no usamos (solo sacamos los que pesan mas de 1mb): ruby-compass ruby liblcms2-2 tk tcl libpq5 libldap-2.4-2 libsasl2-2 openssh-client
# sacamos lo de gnupg2 y node que no seria necesario para nosotros
# tampoco instalamos locales-all porque pesa mucho, hacemos lo de aca abajo

# Other facilities - ADHOC
RUN apt-get -qq update && apt-get install -yqq --no-install-recommends \
    htop wget unzip iputils-ping \
    locales \
    && locale-gen en_US.UTF-8 && update-locale \
    && locale-gen es_AR.UTF-8 && update-locale \
    && echo 'LANG="en_US.UTF-8"' > /etc/default/locale \
    && pip install --no-cache-dir git+https://github.com/OCA/openupgradelib/@master \
    && apt-get -yqq autoremove \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Generate locale (es_AR for right odoo es_AR language config, and C.UTF-8 for postgres and general locale data). TODO better C.UTF-8 or en_US.UTF-8? - ADHOC
ENV LANG es_AR.UTF-8
ENV LANGUAGE es_AR:es:en_US:en
ENV LC_ALL es_AR.UTF-8

# no lo necesitamos - ADHOC
# Special case to get latest Less and PhantomJS
# RUN ln -s /usr/bin/nodejs /usr/local/bin/node \
#     && npm install -g less@2 less-plugin-clean-css@1 phantomjs-prebuilt@2 \
#     && rm -Rf ~/.npm /tmp/*

# no lo necesitamos - ADHOC
# Special case to get bootstrap-sass, required by Odoo for Sass assets
# RUN gem install --no-rdoc --no-ri --no-update-sources bootstrap-sass --version '<4' \
#     && rm -Rf ~/.gem /var/lib/gems/*/cache/

# Execute installation script by Odoo version
# This is at the end to benefit from cache at build time
# https://docs.docker.com/engine/reference/builder/#/impact-on-build-caching
ENV ODOO_SOURCE=odoo/odoo
ENV ODOO_VERSION=13.0

# RUN pip install psycopg2-binary \
RUN debs=" build-essential \
        libfreetype6-dev \
        libfribidi-dev \
        libghc-zlib-dev \
        libharfbuzz-dev \
        libjpeg-dev \
        liblcms2-dev \
        libldap2-dev \
        libopenjp2-7-dev \
        libpq-dev \
        libsasl2-dev \
        libtiff5-dev \
        libwebp-dev \
        tcl-dev \
        tk-dev \
        zlib1g-dev \
    " \
    && apt-get update \
    && apt-get install -yqq --no-install-recommends $debs \
    && pip install \
        -r https://raw.githubusercontent.com/$ODOO_SOURCE/$ODOO_VERSION/requirements.txt \
    && (python3 -m compileall -q /usr/local/lib/python3.7/ || true) \
    # TODo analizar si manual mejor a autoremove
    && apt-get purge -yqq $debs \
    && rm -Rf /var/lib/apt/lists/* /tmp/*

# Metadata
ARG VCS_REF
ARG BUILD_DATE
ARG VERSION
LABEL org.label-schema.schema-version="$VERSION" \
      org.label-schema.vendor=ADHOC \
      org.label-schema.license=Apache-2.0 \
      org.label-schema.build-date="$BUILD_DATE" \
      org.label-schema.vcs-ref="$VCS_REF" \
      org.label-schema.vcs-url="https://github.com/ingadhoc/docker-odoo-adhoc"

USER odoo
