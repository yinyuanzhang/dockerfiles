FROM jenkins

MAINTAINER Delfer <i@delfer.ru>

USER root

RUN    apt-get update \
    && apt-get -y install qemu-utils python-setuptools \
    && export DOCKER_LATEST=$(wget -q https://download.docker.com/linux/static/stable/x86_64/ -O - | grep href | cut -d- -f2 | tail -1) \
    && wget https://download.docker.com/linux/static/stable/x86_64/docker-$DOCKER_LATEST-ce.tgz \
    && tar -xvf docker-*-ce.tgz \
    && mv docker/* /bin/ \
    && rm -rf docker \
    && git clone https://github.com/s3tools/s3cmd.git \
    && cd s3cmd \
    && python setup.py install \
    && cd .. && rm -rf s3cmd
