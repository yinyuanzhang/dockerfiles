FROM nvidia/cuda:10.0-cudnn7-devel-ubuntu18.04
WORKDIR /usr/local

ARG BJ_TZ=/usr/share/zoneinfo/Asia/Shanghai
ENV DEBIAN_FRONTEND noninteractive
RUN rm /etc/apt/sources.list.d/*
COPY sources.list /etc/apt/
COPY pip.conf /tmp/
RUN apt-get update                              && \
    apt-get upgrade -y                          && \
    apt-get install -y apt-utils wget vim          \
    python3.7 python-dev python3.7-dev             \
    build-essential libssl-dev libffi-dev          \
    python3-distutils  libxml2-dev libxslt1-dev    \
    zlib1g-dev tzdata                           && \
    rm -f /etc/localtime                        && \
    ln -sf $BJ_TZ /etc/localtime                && \
    dpkg-reconfigure -f noninteractive tzdata   && \
    wget -O /tmp/get-pip.py                        \
    https://bootstrap.pypa.io/get-pip.py        && \
    rm -f /usr/bin/python3 /usr/bin/python      && \
    ln -s /usr/bin/python3.7 /usr/bin/python3   && \
    ln -s /usr/bin/python3.7 /usr/bin/python    && \
    python /tmp/get-pip.py                      && \
    ln -s /usr/bin/pip3 /usr/bin/pip            && \
    pip install --upgrade pip                   && \
    mkdir ~/.pip                                && \
    mv /tmp/pip.conf ~/.pip/                    && \
    rm -f /tmp/get-pip.py                       && \
    pip install numpy==1.16.4                   && \
    pip install matplotlib==2.2.4               && \
    pip install scipy==1.2.1                    && \
    pip --default-timeout=1000                     \
    install paddlepaddle-gpu==1.5.1.post107

RUN apt-get install -y openssh-server           && \
    mkdir /var/run/sshd                         && \
    echo 'root:123456' |chpasswd      

RUN sed -ri 's/^#?PermitRootLogin\s+.*/PermitRootLogin yes/' /etc/ssh/sshd_config
RUN sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config

RUN mkdir /root/.ssh                                 && \
    apt-get clean                                    && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*    && \
    echo 'export $(cat /proc/1/environ |tr "\\0" "\\n" | xargs)'　>> /etc/profile

EXPOSE 22
CMD    ["/usr/sbin/sshd", "-D"]