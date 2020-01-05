FROM sconecuratedimages/utils:intel-sgx-sdk-2.5

MAINTAINER Florian Österreich <florian.oesterreich@ossmail.de>

RUN apt-get update && apt-get install -y git make gcc g++ bc python xutils-dev bison flex libgcrypt20-dev libjson-c-dev automake autopoint \
    autoconf pkgconf libtool libcurl4-openssl-dev libprotobuf-dev libprotobuf-c-dev protobuf-compiler \
    protobuf-c-compiler libssl-dev wget rsync sed&& \
    git clone https://github.com/lsds/sgx-lkl.git && cd sgx-lkl && \
    sed -i '/.*if(mmap_fixed.*/a if (addr == NULL) {addr = mmap_base;}' /sgx-lkl/src/sgx/enclave_mem.c && \
    make RELEASE=true && make sgx-lkl-sign && make install
