FROM ubuntu:18.04
SHELL ["/bin/bash","-c"]
RUN apt-get -y update && \
    apt-get -y upgrade && \
    DEBIAN_FRONTEND=noninteractive apt-get -y install \
        gcc \
        g++ \
        zlibc \
        zlib1g-dev \
        libssl-dev \
        libbz2-dev \
        libsqlite3-dev \
        libncurses5-dev \
        libgdbm-dev \
        libgdbm-compat-dev \
        liblzma-dev \
        libreadline-dev \
        libffi-dev \
        git \
	ansible \
        bash-completion \
        python3.7 \
	python3-pip \
        libmysqlclient-dev \
        python3.7-dev \
	libpq-dev \
	python-psycopg2 && \
    cd /usr/local/bin && \
    ln -s /usr/bin/python3 python && \
    pip3 install --upgrade pip && \
    apt-get -y autoclean && \
    apt-get -y autoremove && \
    rm -rf /var/lib/apt-get/lists/*
CMD [ "/bin/bash" ]

