FROM iganarix/os-ubuntu-18.04
# https://hub.docker.com/r/iganarix/os-ubuntu-18.04/

MAINTAINER iganari

### Install cmatrix && nyancat
RUN DEBIAN_FRONTEND=noninteractive \
    apt install -y \
                --no-install-recommends \
                cmatrix \
                nyancat

### Install asciiquarium
RUN apt install -y \
                --no-install-recommends \
                libcurses-perl \
                wget \
                unzip \
                make && \
    yes '' | cpan -i YAML && \
    yes '' | cpan -i Term::Animation && \
    cd /usr/local/src && \
    wget https://github.com/cmatsuoka/asciiquarium/archive/master.zip -O asciiquarium.zip && \
    unzip asciiquarium.zip -d /usr/local/src/ && \
    ln -s /usr/local/src/asciiquarium-master/asciiquarium /usr/local/bin/asciiquarium
