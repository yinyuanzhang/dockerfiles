FROM ubuntu:18.04
MAINTAINER Odoo Erp Cloud <info@odooerpcloud.com>

# Generate locale C.UTF-8 for postgres and general locale data
ENV LANG C.UTF-8
ENV TZ=Europe/Madrid
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# Install some deps, lessc and less-plugin-clean-css, and wkhtmltopdf
RUN set -x; \
        apt-get update \
        && apt-get install -y --no-install-recommends \
            ca-certificates \
            curl \
            dirmngr \
            openssh-server \
            fonts-noto-cjk \
            gnupg \
            libssl1.0-dev \
            node-less \
            python3 \
            python3-pip \
            git \
            python3-renderpm \
            python3-watchdog \
            xz-utils \
            gcc \
            python3-dev \
            libxml2-dev \
            libxslt1-dev \
            libevent-dev \
            libsasl2-dev \
            libldap2-dev \
            libpq-dev \
            libpng-dev \
            libjpeg-dev \
        && curl -o wkhtmltox.deb -sSL https://github.com/wkhtmltopdf/wkhtmltopdf/releases/download/0.12.5/wkhtmltox_0.12.5-1.bionic_amd64.deb \
        && echo 'f1689a1b302ff102160f2693129f789410a1708a wkhtmltox.deb' | sha1sum -c - \
        && dpkg --force-depends -i wkhtmltox.deb\
        && apt-get -y install -f --no-install-recommends \
        && rm -rf /var/lib/apt/lists/* wkhtmltox.deb

# install latest postgresql-client
RUN set -x; \
        echo 'deb http://apt.postgresql.org/pub/repos/apt/ bionic-pgdg main' > etc/apt/sources.list.d/pgdg.list \
        && export GNUPGHOME="$(mktemp -d)" \
        && repokey='B97B0AFCAA1A47F044F244A07FCC7D46ACCC4CF8' \
        && gpg --batch --keyserver keyserver.ubuntu.com --recv-keys "${repokey}" \
        && gpg --armor --export "${repokey}" | apt-key add - \
        && gpgconf --kill all \
        && rm -rf "$GNUPGHOME" \
        && apt-get update  \
        && apt-get install -y postgresql-client \
        && rm -rf /var/lib/apt/lists/*

# Install rtlcss (on Debian stretch)
RUN set -x;\
    echo "deb http://deb.nodesource.com/node_8.x bionic main" > /etc/apt/sources.list.d/nodesource.list \
    && export GNUPGHOME="$(mktemp -d)" \
    && repokey='9FD3B784BC1C6FC31A8A0A1C1655A0AB68576280' \
    && gpg --batch --keyserver keyserver.ubuntu.com --recv-keys "${repokey}" \
    && gpg --armor --export "${repokey}" | apt-key add - \
    && gpgconf --kill all \
    && rm -rf "$GNUPGHOME" \
    && apt-get update \
    && apt-get install -y nodejs \
    && npm install -g rtlcss \
    && rm -rf /var/lib/apt/lists/*

# Install Odoo
ENV ODOO_VERSION 13.0

# Copy entrypoint script and Odoo configuration file
RUN apt update && apt install -y python3-setuptools
RUN pip3 install unicodecsv unidecode pysftp==0.2.8 libsass
COPY ./entrypoint.sh /

# Mount /var/lib/odoo to allow restoring filestore and /mnt/extra-addons for users addons
RUN mkdir -p /opt/odoo/extra-addons \
    && mkdir -p /opt/odoo/data \
    && mkdir -p /opt/odoo/config

COPY ./odoo.conf /opt/odoo/config

VOLUME ["/opt/odoo/data", "/opt/odoo/extra-addons", "/var/lib/odoo"]

# Clone Odoo and Other Repositories
RUN git clone https://github.com/odoo/odoo.git -b $ODOO_VERSION --depth 1 /opt/odoo/odoo
RUN pip3 install -r /opt/odoo/odoo/requirements.txt

# --------SSH service --
ARG set_ssh_port=8089
ARG debug_odoo_port=9090
ARG set_root_passwd=root
RUN mkdir /var/run/sshd
RUN echo "root:$set_root_passwd" |chpasswd
RUN sed -ri "s/^#?PermitRootLogin\s+.*/PermitRootLogin yes/" /etc/ssh/sshd_config
RUN sed -ri "s/UsePAM yes/#UsePAM yes/g" /etc/ssh/sshd_config
RUN sed -ri "s/#Port 22/Port ${set_ssh_port}/g" /etc/ssh/sshd_config

RUN mkdir /root/.ssh
COPY authorized_keys /root/.ssh
# RUN ssh-keygen -t rsa -f /etc/ssh/ssh_host_rsa_key -A -q -N ""

RUN apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# -----------
# Expose Odoo services
EXPOSE 8069 8071 ${set_ssh_port} ${debug_odoo_port}

# Set the default config file
ENV ODOO_RC /opt/odoo/config/odoo.conf

COPY wait-for-psql.py /usr/local/bin/wait-for-psql.py

# Set default user when running the container
RUN ln -s /opt/odoo/odoo/odoo-bin /usr/bin/odoo
CMD ["/usr/sbin/sshd", "-D"]

ENTRYPOINT ["/entrypoint.sh"]
CMD ["odoo"]


