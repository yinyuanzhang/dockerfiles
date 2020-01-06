FROM python:3.6

ADD https://github.com/vishnubob/wait-for-it/raw/master/wait-for-it.sh /usr/local/bin/
RUN set -eux; \
    chmod +x /usr/local/bin/wait-for-it.sh; \
    apt-get update -y; \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
        build-essential \
        bzip2 \
        git \
        libev-dev \
        make \
        p7zip-full \
        rsync \
        tar \
        xz-utils \
        zip \
        ; \
    apt-get clean; \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN pip --no-cache-dir install --upgrade \
        ansible \
        bjoern \
        psycopg2-binary \
        poetry \
        pytest \
        pytest-timeout \
        setuptools \
        testinfra \
        ;
