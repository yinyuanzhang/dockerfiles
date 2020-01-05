# base image from https://github.com/matthewfeickert/Docker-Python3-Ubuntu/blob/master/Dockerfile

FROM ubuntu:bionic

USER root
WORKDIR /root

SHELL [ "/bin/bash", "-c" ]

ARG PYTHON_VERSION_TAG=3.6.0
ARG LINK_PYTHON_TO_PYTHON3=1

# Existing lsb_release causes issues with modern installations of Python3
# https://github.com/pypa/pip/issues/4924#issuecomment-435825490
# Set (temporarily) DEBIAN_FRONTEND to avoid interacting with tzdata
RUN apt-get -qq -y update && \
    apt-get -qq -y upgrade && \
    DEBIAN_FRONTEND=noninteractive apt-get -qq -y install \
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
        uuid-dev \
        libffi-dev \
        tk-dev \
        wget \
        curl \
        git \
        make \
        sudo \
        bash-completion \
        tree \
        vim \
        oathtool \
        software-properties-common && \
    mv /usr/bin/lsb_release /usr/bin/lsb_release.bak && \
    apt-get -y autoclean && \
    apt-get -y autoremove && \
    rm -rf /var/lib/apt-get/lists/*

RUN add-apt-repository -r ppa:deadsnakes/ppa && \
    apt-get update && \
    apt-get install python3.6

RUN python3.6 --version
RUN apt install -y python3-pip && \
    python3.6 -m pip install pip

RUN pip3 install pandas
RUN pip3 install 'joblib<=0.13.99,>=0.11' --force-reinstall
RUN pip3 install 'jsonschema<=3,>=2.5.1' --force-reinstall
RUN pip3 install 'webdriver-manager==2.2.0' --force-reinstall
RUN pip3 install flask --force-reinstall

ARG port=2020
ENV CIVIS_SERVICE_PORT=2020

COPY entrypoint.sh /

EXPOSE 2020

ENTRYPOINT ["/entrypoint.sh"]