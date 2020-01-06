FROM ubuntu
MAINTAINER Li Kang 

ENV DEBIAN_FRONTEND noninteractive
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  

RUN apt-get -qq update \
    && apt-get install -y build-essential ca-certificates curl \
        git libcurl4-openssl-dev libffi-dev libjpeg-dev \
        libmysqlclient-dev libpng12-dev libpq-dev libsqlite3-dev \
        libssl-dev libxml2-dev libxslt1-dev libz-dev mercurial \
        wget zlib1g-dev --no-install-recommends \
    && apt-get install -y python3 python3-pip python3-setuptools \
        python3-dev --no-install-recommends \
    && pip3 install --upgrade pip setuptools \
    && apt-get install -y mysql-server --no-install-recommends \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

