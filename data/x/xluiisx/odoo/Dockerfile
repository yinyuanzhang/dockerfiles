FROM ubuntu:18.04
MAINTAINER Luis Triana <luis.triana@jarsa.com.mx>

RUN echo 'APT::Get::Assume-Yes "true";' >> /etc/apt/apt.conf
RUN apt-get update \
    && apt-get install sudo gnupg language-pack-es -y \
    && locale-gen "en_US.UTF-8" "fr_FR.UTF-8"
ENV LANG="en_US.UTF-8" LANGUAGE="en_US.UTF-8" LC_ALL="en_US.UTF-8" \
    PYTHONIOENCODING="UTF-8" TERM="xterm" DEBIAN_FRONTEND="noninteractive"
RUN apt-get update -q && apt-get upgrade -q && \
    apt-get install --allow-unauthenticated -q \
        wget \
        curl
RUN curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
RUN apt-get install -y nodejs
RUN curl -sL https://dl.yarnpkg.com/debian/pubkey.gpg | sudo apt-key add -
RUN apt-get update && apt-get install yarn
RUN echo 'deb http://apt.postgresql.org/pub/repos/apt/ bionic-pgdg main' >> /etc/apt/sources.list.d/pgdg.list && \
    wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | \
    sudo apt-key add -
RUN echo 'deb http://security.ubuntu.com/ubuntu xenial-security main' >> /etc/apt/sources.list
RUN apt-get update -q && apt-get upgrade -q && \
    apt-get install --allow-unauthenticated -q \
        aptitude \
        build-essential \
        fontconfig \
        git \
        libevent-dev \
        libjpeg-dev \
        libldap2-dev \
        libsasl2-dev \
        libssl-dev \
        libffi-dev \
        libpq-dev \
        libx11-6 \
        libxext6 \
        libxml2-dev \
        libxrender1 \
        libxslt-dev \
        nano \
        node-less \
        openssl \
        postgresql-server-dev-9.5 \
        postgresql-9.5 \
        postgresql-client-9.5 \
        postgresql-contrib-9.5 \
        python \
        python-dev \
        python-pip \
        python-pil \
        python-libxml2 \
        python-pandas \
        python-psycopg2 \
        xfonts-75dpi \
        xfonts-base \
        python-qrtools \
        python-openssl \
        openssh-server \
        swig \
        xmlstarlet \
        xsltproc 

    # Install wkhtmltopdf
RUN cd /tmp && \
    wget -O wkhtmltox_0.12.5-1.bionic_amd64.deb https://downloads.wkhtmltopdf.org/0.12/0.12.5/wkhtmltox_0.12.5-1.bionic_amd64.deb && \
    dpkg -i wkhtmltox_0.12.5-1.bionic_amd64.deb

# Download and install odoo requirements from github.com/odoo/odoo/requirements.txt
RUN cd /tmp && \
    wget -q https://raw.githubusercontent.com/odoo/odoo/10.0/requirements.txt && \
    pip install -r requirements.txt && pip install --upgrade pip

#Python Libraries
RUN pip install suds \
    pyopenssl \
    M2Crypto \
    pillow \
    qrcode \
    xmltodict \
    xlrd \
    cfdilib \
    pytz \
    jinja2 \
    json2html \
    odoorpc \
    ofxparse \
    num2words \
    boto3 \
    cryptography \
    pycrypto

# Cleanup
RUN apt-get clean && rm -rf /var/lib/apt/lists/* && rm -rf /tmp/*

# Add ODOO user
RUN adduser --home=/home/odoo-10.0/ --disabled-password --gecos "" --shell=/bin/bash odoo
RUN echo 'root:odoo**' | chpasswd 
RUN echo "odoo ALL=(root) NOPASSWD:ALL" | tee -a /etc/sudoers.d/user && \
    chmod 0440 /etc/sudoers.d/user

# Create odoo-server.conf
ADD files/odoo-server.conf /home/odoo-10.0/odoo-server.conf
RUN chown odoo /home/odoo-10.0/odoo-server.conf && \
    chmod +x /home/odoo-10.0/odoo-server.conf

#Install Odoo
RUN cd /home/odoo-10.0/ && git clone -b 10.0 --single-branch --depth=1 https://github.com/odoo/odoo.git odoo
RUN chown -R odoo:odoo /home/ && chmod +x /home/odoo-10.0/odoo
RUN mkdir -p /home/.local/share/Odoo/filestore && \
    chown -R odoo:odoo /home/.local/share/Odoo/filestore

RUN mkdir -p /home/odoo-10.0/extra-addons \
        && chown -R odoo /home/odoo-10.0/extra-addons
VOLUME ["/home/.local/share/Odoo/filestore", "/home/odoo-10.0/extra-addons", "/home/odoo-10.0/"]

# Add entrypoint file and give execute permission
ADD files/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Correct error with ssl-cert permissions for Postgres
RUN mkdir /etc/ssl/private-copy && \
    mv /etc/ssl/private/* /etc/ssl/private-copy/ && \
    rm -r /etc/ssl/private && \
    mv /etc/ssl/private-copy /etc/ssl/private && \
    chmod -R 0700 /etc/ssl/private && \
    chown -R postgres /etc/ssl/private

USER postgres

# Run Postgres Server
RUN /etc/init.d/postgresql start && \
    psql --command "CREATE USER odoo WITH SUPERUSER PASSWORD 'odoo';"

USER odoo

CMD /entrypoint.sh

EXPOSE 8069
EXPOSE 8072
EXPOSE 22
EXPOSE 5432
