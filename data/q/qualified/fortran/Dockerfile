FROM ubuntu:18.04

RUN set -ex; \
    useradd --create-home -u 9999 codewarrior; \
    mkdir /workspace; \
    chown codewarrior:codewarrior /workspace;

RUN set -ex; \
    apt-get update; \
    apt-get install -y --no-install-recommends \
        software-properties-common \
    ; \
    add-apt-repository ppa:ubuntu-toolchain-r/test; \
    apt-get update; \
    apt-get install -y --no-install-recommends \
        gfortran-9 \
        wget \
        ca-certificates \
    ; \
    update-alternatives --install /usr/bin/gfortran gfortran /usr/bin/gfortran-9 100; \
    rm -rf /var/lib/apt/lists/*;

RUN set -ex; \
    mkdir -p /runner/frameworks/fortran; \
    cd /runner/frameworks/fortran; \
    wget -q -O cw-2.f95 https://raw.githubusercontent.com/Codewars/fortran-test-framework/v0.0.1/cw-2.f95; \
    gfortran -Wall -fall-intrinsics -std=f2018 -c cw-2.f95; \
    rm cw-2.f95;

USER codewarrior
WORKDIR /workspace
