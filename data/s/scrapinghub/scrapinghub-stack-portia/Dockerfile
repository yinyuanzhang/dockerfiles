FROM python:2
ARG APT_PROXY
ARG PIP_INDEX_URL
ARG PIP_TRUSTED_HOST
ONBUILD ENV PIP_TRUSTED_HOST=$PIP_TRUSTED_HOST PIP_INDEX_URL=$PIP_INDEX_URL
ONBUILD RUN test -n $APT_PROXY && echo 'Acquire::http::Proxy \"$APT_PROXY\";' \
    >/etc/apt/apt.conf.d/proxy

# TERM needs to be set here for exec environments
# PIP_TIMEOUT so installation doesn't hang forever
ENV TERM=xterm \
    PIP_TIMEOUT=180

RUN apt-get update -qq && \
    apt-get install -qy \
        netbase ca-certificates apt-transport-https \
        build-essential locales \
        libdb5.3-dev \
        libxml2-dev \
        libssl-dev \
        libxslt1-dev \
        libevent-dev \
        libffi-dev \
        libpcre3-dev \
        libz-dev \
        unixodbc unixodbc-dev \
        telnet vim htop iputils-ping curl wget lsof git sudo \
        ghostscript
# http://unix.stackexchange.com/questions/195975/cannot-force-remove-directory-in-docker-build
#        && rm -rf /var/lib/apt/lists

# adding custom locales to provide backward support with scrapy cloud 1.0
COPY locales /etc/locale.gen
RUN locale-gen

# Proper path to locate portia-entrypoint by its alias
ENV PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
# Setting environment for bsddb3 install (deltafetch addon)
ENV BERKELEYDB_DIR=/usr

COPY requirements.txt /requirements-portia.txt
RUN pip install --no-cache-dir -r requirements-portia.txt

RUN mkdir /app
COPY addons_eggs /app/addons_eggs
RUN chown nobody:nogroup -R /app/addons_eggs

WORKDIR /scrapy

COPY portia-entrypoint /usr/local/sbin/
RUN chmod +x /usr/local/sbin/portia-entrypoint && \
    ln -s /usr/local/sbin/portia-entrypoint /usr/local/sbin/start-crawl
