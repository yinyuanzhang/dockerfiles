FROM ubuntu:bionic

MAINTAINER maik.dybek@zyxel.eu

# Update apt list
RUN apt-get update --fix-missing && apt-get install -y --no-install-recommends apt-utils

# Install build requirements
# TODO: clean-up list, maybe too excessive installing here...
RUN apt-get install -y libtool zlib1g-dev tofrodos sharutils doxygen ncurses-dev
RUN apt-get install -y xsltproc libstdc++5 subversion autotools-dev g++ g++-4.8 tftp-hpa tftpd-hpa
RUN apt-get install -y zlib1g-dev sharutils patch mysql-common mtd-utils m4 libtool libsvn1 libstdc++-7-dev
RUN apt-get install -y diffstat libneon27-gnutls libpq5 liblzo2-2 libapr1 libaprutil1 libltdl7-dev
RUN apt-get install -y libxml-xpath-perl libclone-perl libdata-compare-perl libxml-libxml-simple-perl
RUN apt-get install -y cifs-utils lzop gtk-doc-tools xsltproc libncurses-dev
RUN apt-get install -y quilt xutils-dev expat graphviz autopoint

# Set timezone to suppress interactive tzdata config caused
# by tcl8.6
RUN ln -sf /usr/share/zoneinfo/Europe/Berlin /etc/localtime

RUN apt-get install -y tcl8.6 libmysqlclient20
RUN apt-get install -y gawk build-essential
RUN apt-get install -y software-properties-common
RUN apt-get install -y byobu curl htop man unzip vim wget
RUN apt-get install -y flex bison tcl automake autoconf xsltproc
RUN apt-get install -y squashfs-tools libtool autotools-dev libncurses-dev
RUN apt-get install -y tofrodos cifs-utils libxml2-utils subversion
RUN apt-get install -y quilt graphviz expat diffstat autopoint
RUN apt-get install -y zlibc zlib1g zlib1g-dev
RUN apt-get install -y lzop
RUN apt-get install -y libexpat1-dev
RUN apt-get install -y libdbus-1-dev
RUN apt-get install -y git-buildpackage
RUN apt-get install -y parallel
RUN apt-get install -y bc
RUN apt-get install -y rsync

# ubifs images
RUN apt-get install -y mtd-utils

# necessary for v4-buildspecs
RUN apt-get install -y python3-yaml

# Ubuntu 16.04 and later
# required for Host builds
RUN apt-get install -y libtool-bin

# Required for Kernel generate modules.dep
RUN apt-get install -y kmod

# necessary for some Python-based unit tests with TAP output, e.g. in config-utilities
RUN apt-get install -y python-pytest python-pip
RUN pip install pytest-tap

# Commandline JSON processor needed for scripts like './btools/bin/headbuild.sh platform-sdk <id>'...
RUN apt-get install -y jq

# install required 32bit libraries (e.g. for slk tool - servicemanager)
RUN dpkg --add-architecture i386
RUN apt-get update
RUN apt-get install -y libc6:i386 libncurses5:i386 libstdc++6:i386

# for building TR-069 components
RUN apt-get install -y libxml2-dev
RUN perl -MCPAN -e 'install Algorithm::Diff'
RUN perl -MCPAN -e 'install Clone'
RUN perl -MCPAN -e 'install Data::Compare'
RUN perl -MCPAN -e 'install URI::Split'
RUN perl -MCPAN -e 'install XML::LibXML'
RUN perl -MCPAN -e 'install XML::XPath'
RUN perl -MCPAN -e 'install String::Tokenizer'

# Install CPP checkstyle tool
RUN apt install -y vera++

# Install Bats: Bash Automated Testing System
RUN apt install -y bats

# Install Sphairon MIPS toolchain
ADD gemini-cross-toolchains/mips-sphairon-linux-uclibc-v2013.03.tar.bz2 /opt
RUN chown -R root:root /opt

# Some newer components use cmake
RUN apt-get install -y cmake

# install git-lfs needed for some repositories
# curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.deb.sh > git-lfs-install-script.deb.sh
COPY git-lfs-install-script.deb.sh .
RUN bash git-lfs-install-script.deb.sh \
    && rm git-lfs-install-script.deb.sh \
    && apt-get install git-lfs

# install jfrog cli to archieve build artifacts
RUN curl -fL https://getcli.jfrog.io | sh \
    && chmod a+rx jfrog \
    && mv jfrog /usr/local/bin/

# Clean up apt to save space
RUN apt-get clean
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Set environment variables.
# define home directory

ARG uid=1000
ARG gid=1000
ARG user=heinzm

RUN groupadd -r -g ${gid} ${user} \
    && useradd -r -u ${uid} -g ${user} -s /usr/sbin/nologin -m -d /home/${user} ${user}

RUN mkdir -p /work
RUN chown ${uid}:${gid} /work

# Switch to a real bash
RUN ln -sf bash /bin/sh

# install script to check for installed components
COPY run_docker_tests.sh /work
RUN chmod a+rx /work/run_docker_tests.sh

# define the default user when starting the container
# give user with docker run -u
USER $user

# Define working directory.
WORKDIR /work/gemini

# Define default command.
CMD ["bash"]
