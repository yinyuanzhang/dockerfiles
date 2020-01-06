FROM gcc:6

ENV CMAKE_SIG_KEY_FP CBA23971357C2E6590D9EFD3EC8FEF3A7BFB4EDA
ENV CMAKE_MINOR_VERSION 3.7
ENV CMAKE_VERSION 3.7.2


ADD "https://cmake.org/files/v${CMAKE_MINOR_VERSION}/cmake-${CMAKE_VERSION}-Linux-x86_64.sh" /tmp
ADD "https://cmake.org/files/v${CMAKE_MINOR_VERSION}/cmake-${CMAKE_VERSION}-SHA-256.txt" /tmp
ADD "https://cmake.org/files/v${CMAKE_MINOR_VERSION}/cmake-${CMAKE_VERSION}-SHA-256.txt.asc" /tmp

RUN gpg --keyserver pgp.mit.edu --recv-keys ${CMAKE_SIG_KEY_FP} \
    && echo "${CMAKE_SIG_KEY_FP}:6:" | gpg --import-ownertrust

RUN /bin/bash -c "pushd /tmp \
    && gpg --batch --verbose --verify cmake-${CMAKE_VERSION}-SHA-256.txt.asc cmake-${CMAKE_VERSION}-SHA-256.txt \
    && (grep -- '-Linux-x86_64.sh$' cmake-${CMAKE_VERSION}-SHA-256.txt | sha256sum -c ) \
    && mkdir -p /opt/cmake \
    && sh cmake-${CMAKE_VERSION}-Linux-x86_64.sh --prefix=/opt/cmake --skip-license --exclude-subdir \
    && popd"

