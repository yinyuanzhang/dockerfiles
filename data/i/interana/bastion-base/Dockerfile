FROM ubuntu:18.04 as bastion_base

RUN apt-get update && apt-get upgrade -y &&  \
    apt-get install -y \
    git libffi-dev libssl-dev libncurses5-dev libjpeg8-dev wget curl make gcc zlib1g-dev \
    python-pip python-dev python2.7 python3 python3-pip python3-venv openssh-server vim mysql-client && \
    rm -rf /var/lib/apt/lists/*

RUN python -m pip install --upgrade pip && \
    pip3 install --upgrade pip && \
    pip install readline virtualenv virtualenvwrapper

RUN wget https://gnupg.org/ftp/gcrypt/gnupg/gnupg-1.4.23.tar.bz2 && tar xjf gnupg-1.4.23.tar.bz2 && cd gnupg-1.4.23 && ./configure && make && make install
