FROM xcgd/ubuntu4base:xenial
MAINTAINER alexandre.allouche@xcg-consulting.fr

# Install this beforehand in order to add https PPA providers.
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get -yq install locales apt-transport-https 

ADD files /

# generate locales
RUN locale-gen

ENV LANG en_US.UTF-8

# Add the PostgreSQL PGP key to verify their Debian packages.
RUN apt-key add /var/tmp/ACCC4CF8.asc && rm /var/tmp/ACCC4CF8.asc

# Add PostgreSQL's repository. It contains the most recent stable release
#     of PostgreSQL, ``9.6``.
# install dependencies as distrib packages when system bindings are required
# some of them extend the basic odoo requirements for a better "apps" compatibility
# some dependencies are distributed as wheel packages at the next step
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get -yq install --no-install-recommends \
    adduser \
    ghostscript \
# maybe used in odoo 9 to determine mime type
    file \
    python2.7 \
    node-less \
    postgresql-client-9.6 \
    python-setuptools python-wheel python-pip \
    python-six \
    python-lxml \
    python-babel \
    python-cffi \
    python-contextlib2 \
    python-dateutil \
    python-decorator \
    python-docutils \
    python-feedparser \
    python-gdata \
    python-genshi \
    python-gevent \
    python-greenlet \
    python-jinja2 \
    python-ldap \
    python-mako \
    python-markupsafe \
    python-mock \
    python-msgpack \
    python-openid \
    python-openssl \
    python-passlib \
    python-psutil \
    python-psycogreen \
    python-psycopg2 \
    python-pydot \
    python-pygraphviz \
    python-pyparsing \
    python-pil \
    python-qrcode \
    python-reportlab \
    python-serial \
    python-simplejson \
    python-stdnum \
    python-suds \
    python-unittest2 \
    python-usb \
    python-vatnumber \
    python-vobject \
    python-webdav \
    python-werkzeug \
    python-xlwt \
    python-yaml \
    python-zmq \
    python-cryptography \
    python-pychart python-libxslt1 xfonts-base xfonts-75dpi \
    libxrender1 libxext6 fontconfig \
#    python-zsi \
    liblasso3 python-lasso \
    unzip \
    libzmq5

# use wheels from pypi
# these are python dependencies for odoo and "apps" as precompiled wheel packages

RUN pip install --disable-pip-version-check --no-cache-dir --system --only-binary wheel --require-hashes -r /var/tmp/requirements

# install wkhtmltopdf based on QT5
ADD https://downloads.wkhtmltopdf.org/0.12/0.12.5/wkhtmltox_0.12.5-1.xenial_amd64.deb /var/tmp/wkhtmltox.deb
RUN apt install /var/tmp/wkhtmltox.deb && rm -f /var/tmp/wkhtmltox.deb

# create the odoo user
RUN adduser --home=/opt/odoo --disabled-password --gecos "" --shell=/bin/bash odoo

# changing user is required by odoo which won't start with root
# makes the container more unlikely to be unwillingly changed in interactive mode
USER odoo

# ADD sources for the oe components
ADD --chown=odoo:odoo https://github.com/OCA/OpenUpgrade/archive/9.0.zip /opt/odoo/odoo.zip

RUN /bin/bash -c "mkdir -p /opt/odoo/{{etc,sources,additional_addons,data},/var/{run,log,egg-cache}}" && \
    cd /opt/odoo/sources && \
    unzip -q /opt/odoo/odoo.zip && \
    mv OpenUpgrade-9.0 odoo && \
    rm /opt/odoo/odoo.zip

# Execution environment
USER 0
# To install, we need to remove PIL from requirements and use Pillow (that include PIL)
# Gunicorn need the application to be installed
RUN cd /opt/odoo/sources/odoo && \
    pip install --disable-pip-version-check --no-cache-dir --system . --no-deps && \
    mv /opt/odoo/sources/odoo/addons /var/tmp/addons && \
    rm -rf /opt/odoo/sources/odoo && \
    mkdir /opt/odoo/sources/odoo && \
    mv /var/tmp/addons /opt/odoo/sources/odoo
VOLUME ["/opt/odoo/var", "/opt/odoo/etc", "/opt/odoo/additional_addons", "/opt/odoo/data"]
# Set the default entrypoint (non overridable) to run when starting the container
ENTRYPOINT ["/usr/local/bin/boot"]
CMD ["help"]
# Expose the odoo ports (for linked containers)
EXPOSE 8069 8072
