FROM continuumio/miniconda3

# Never prompts the user for choices on installation/configuration of packages
ENV DEBIAN_FRONTEND noninteractive
ENV TERM linux

ENV PYTHONIOENCODING UTF-8
ENV PYTHONUNBUFFERED 0

RUN set -ex \
    && export CPLUS_INCLUDE_PATH="$CPLUS_INCLUDE_PATH:/usr/include/python2.7/" \
    && buildDeps=' \
        build-essential \
        python-dev \
        python3-dev \
        libkrb5-dev \
        libsasl2-modules \
        libsasl2-dev \
        libssl-dev \
        libffi-dev \
        libxslt-dev \
        libxml2-dev \
        build-essential \
        libblas-dev \
        liblapack-dev \
        libpq-dev \
        locales \
    ' \
    && apt-get update -yqq \
    && apt-get upgrade -yqq \
    && apt-get install -yqq --no-install-recommends $buildDeps \
    && apt-get install -yqq apt-utils \
    && rm -rf /var/lib/apt/lists/* \
    && echo "Europe/Ireland" > /etc/timezone \
    && dpkg-reconfigure -f noninteractive tzdata \
    && sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen \
    && echo 'LANG="en_US.UTF-8"'>/etc/default/locale \
    && locale-gen en en_US en_US.UTF-8 \
    && dpkg-reconfigure --frontend=noninteractive locales \
    && update-locale LANG=en_US.UTF-8 \
    && apt-get clean \
    && locale

ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8
