# Build boxyd from source and set image to stay alive.


FROM ubuntu:16.04

ENV SOURCE_ORIGIN https://github.com/boxycoin/boxycoinv3.1.git
ENV COMMIT 7e9e3040f906b3d14225f8811425f0e40cd5f5ce
ENV SOURCE_LOCAL_ROOT /root/boxycoinv3.1

WORKDIR /root

# 1. We need to do this first in order to see any packages at all
RUN apt-get update \
    # 2. Install the basic foundation of build tools.
    && apt-get install -y --no-install-recommends \
       build-essential \
       libssl-dev \
       libtool \
       openssl \
       pkg-config \
       wget \
       python-dev \
       autotools-dev \
       software-properties-common \
       autoconf \
       automake \
       libzmq3-dev \
       libminiupnpc-dev \
       libevent-dev \
       libgmp-dev \
    # 3. We don't need all of the boost libraries, only selectively install a handful of them
    && apt-get install -y --no-install-recommends \
       libboost-chrono-dev \
       libboost-filesystem-dev \
       libboost-program-options-dev \
       libboost-system-dev \
       libboost-test-dev \
       libboost-thread-dev \
    # 4. We need this because we want to get v4.8 of the wallet db
    && add-apt-repository ppa:bitcoin/bitcoin \
    # 4.2 And now we need to update this again
    && apt-get update \
    # 4.3 Now get v4.8 of the wallet db
    && apt-get install -y --no-install-recommends libdb4.8-dev libdb4.8++-dev \
    # 5. Now clone the source code.
    && apt-get install -y --no-install-recommends \
       ca-certificates \
       git \
    && git clone $SOURCE_ORIGIN
RUN cd $SOURCE_LOCAL_ROOT \
    # We happen to know that this particular commit works.
    && git checkout $COMMIT \
    # 9. Now build boxyd
    && cd $SOURCE_LOCAL_ROOT/src/leveldb \
    && wget https://github.com/google/leveldb/archive/v1.18.tar.gz \
    && tar xfv v1.18.tar.gz \
    && cp leveldb-1.18/Makefile $SOURCE_LOCAL_ROOT/src/leveldb/ \
    && cd $SOURCE_LOCAL_ROOT/src \
    && chmod +x leveldb/build_detect_platform \
    && make -f makefile.unix USE_UPNP=-
    # At this point, boxyd should be useable.
RUN cd $SOURCE_LOCAL_ROOT/src \
    && chmod 755 boxyd \
    && strip $SOURCE_LOCAL_ROOT/src/boxyd \
    && cp $SOURCE_LOCAL_ROOT/src/boxyd /usr/local/bin \
    # 12. Establish a datadir.
    && mkdir /root/.boxy

# a few minor docker-specific tweaks
# see https://github.com/docker/docker/blob/9a9fc01af8fb5d98b8eec0740716226fadb3735c/contrib/mkimage/debootstrap
RUN set -xe \
	\
# https://github.com/docker/docker/blob/9a9fc01af8fb5d98b8eec0740716226fadb3735c/contrib/mkimage/debootstrap#L40-L48
	&& echo '#!/bin/sh' > /usr/sbin/policy-rc.d \
	&& echo 'exit 101' >> /usr/sbin/policy-rc.d \
	&& chmod +x /usr/sbin/policy-rc.d \
	\
# https://github.com/docker/docker/blob/9a9fc01af8fb5d98b8eec0740716226fadb3735c/contrib/mkimage/debootstrap#L54-L56
	&& dpkg-divert --local --rename --add /sbin/initctl \
	&& cp -a /usr/sbin/policy-rc.d /sbin/initctl \
	&& sed -i 's/^exit.*/exit 0/' /sbin/initctl \
	\
# https://github.com/docker/docker/blob/9a9fc01af8fb5d98b8eec0740716226fadb3735c/contrib/mkimage/debootstrap#L71-L78
	&& echo 'force-unsafe-io' > /etc/dpkg/dpkg.cfg.d/docker-apt-speedup \
	\
# https://github.com/docker/docker/blob/9a9fc01af8fb5d98b8eec0740716226fadb3735c/contrib/mkimage/debootstrap#L85-L105
	&& echo 'DPkg::Post-Invoke { "rm -f /var/cache/apt/archives/*.deb /var/cache/apt/archives/partial/*.deb /var/cache/apt/*.bin || true"; };' > /etc/apt/apt.conf.d/docker-clean \
	&& echo 'APT::Update::Post-Invoke { "rm -f /var/cache/apt/archives/*.deb /var/cache/apt/archives/partial/*.deb /var/cache/apt/*.bin || true"; };' >> /etc/apt/apt.conf.d/docker-clean \
	&& echo 'Dir::Cache::pkgcache ""; Dir::Cache::srcpkgcache "";' >> /etc/apt/apt.conf.d/docker-clean \
	\
# https://github.com/docker/docker/blob/9a9fc01af8fb5d98b8eec0740716226fadb3735c/contrib/mkimage/debootstrap#L109-L115
	&& echo 'Acquire::Languages "none";' > /etc/apt/apt.conf.d/docker-no-languages \
	\
# https://github.com/docker/docker/blob/9a9fc01af8fb5d98b8eec0740716226fadb3735c/contrib/mkimage/debootstrap#L118-L130
	&& echo 'Acquire::GzipIndexes "true"; Acquire::CompressionTypes::Order:: "gz";' > /etc/apt/apt.conf.d/docker-gzip-indexes \
	\
# https://github.com/docker/docker/blob/9a9fc01af8fb5d98b8eec0740716226fadb3735c/contrib/mkimage/debootstrap#L134-L151
	&& echo 'Apt::AutoRemove::SuggestsImportant "false";' > /etc/apt/apt.conf.d/docker-autoremove-suggests

# delete all the apt list files since they're big and get stale quickly
RUN rm -rf /var/lib/apt/lists/*
# this forces "apt-get update" in dependent images, which is also good
# (see also https://bugs.launchpad.net/cloud-images/+bug/1699913)

# make systemd-detect-virt return "docker"
# See: https://github.com/systemd/systemd/blob/aa0c34279ee40bce2f9681b496922dedbadfca19/src/basic/virt.c#L434
RUN mkdir -p /run/systemd && echo 'docker' > /run/systemd/container

EXPOSE 3335
EXPOSE 3336

# Define our command to be run when launching the container
CMD exec /bin/bash -c "boxyd -daemon & trap : TERM INT; sleep infinity & wait"