FROM ubuntu:18.04
ARG TIMEZONE
RUN apt update && apt install -y tzdata
RUN echo ${TIMEZONE} > /etc/timezone
RUN rm -f /etc/localtime
RUN dpkg-reconfigure -f noninteractive tzdata
RUN apt -q update && apt -qq install -y \
    build-essential \
    checkinstall \
    libreadline-gplv2-dev \
    libncursesw5-dev \
    libssl-dev \
    libsqlite3-dev \
    tk-dev \
    libgdbm-dev \
    libc6-dev \
    libbz2-dev \
    zlib1g-dev \
    openssl \
    libffi-dev \
    python3-dev \
    python3-setuptools \
    wget \
    libssl1.0.0 \
    unzip \
    && mkdir /tmp/Python37
WORKDIR /tmp/Python37
RUN wget https://www.python.org/ftp/python/3.7.2/Python-3.7.2.tar.xz \
    && tar xvf Python-3.7.2.tar.xz
WORKDIR /tmp/Python37/Python-3.7.2
RUN ./configure --enable-optimizations > /dev/null 2>&1 \
    && make altinstall > /dev/null 2>&1
ADD ./rikabot/requirements.txt /opt/rikabot/requirements.txt
WORKDIR /opt/rikabot
RUN apt -qq install -y \
        pgloader \
        libffi-dev \
        libnacl-dev
RUN python3.7 -m pip install -r requirements.txt
RUN rm requirements.txt
RUN rm -r /tmp/Python37
CMD python3.7 rikabot.py
