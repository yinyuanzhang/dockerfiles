FROM buildpack-deps:bionic

ENV LANG=C.UTF-8

RUN set -ex; \
# Specifying user id because the file owner seems to revert to root if the user has
# the same uid (commonly 1000) as the user on host when userns-remap is enabled.
# https://github.com/moby/moby/issues/39169
    useradd --create-home -u 9999 codewarrior; \
    mkdir -p /workspace; \
    chown -R codewarrior:codewarrior /workspace;

RUN set -ex; \
    wget -q -O - https://github.com/Snaipe/Criterion/releases/download/v2.3.3/criterion-v2.3.3-linux-x86_64.tar.bz2 | tar xj -C /usr --strip-components=1; \
    wget -q -O - https://apt.llvm.org/llvm-snapshot.gpg.key | apt-key add -; \
    mkdir -p /etc/apt/sources.list.d/; \
    echo "deb http://apt.llvm.org/bionic/ llvm-toolchain-bionic-8 main" > /etc/apt/sources.list.d/clang-8.list; \
    apt-get update; \
    apt-get install -y --no-install-recommends software-properties-common; \
    add-apt-repository ppa:ubuntu-toolchain-r/test; \
    apt-get update; \
    apt-get install -y --no-install-recommends \
        cmake \
        clang-8 \
        gcc-9 \
        g++-9 \
    ; \
    cd /tmp; \
    git clone --recursive --depth 1 --branch codewars https://github.com/kazk/igloo.git; \
    mkdir -p igloo/build; \
    cd igloo/build; \
    cmake ..; \
    make install; \
    apt-get remove -y cmake; \
    apt-get autoremove -y; \
    apt-get clean; \
    rm -rf /var/lib/apt/lists/* /tmp/*;

COPY rootfs/opt/runner /opt/runner
RUN set -ex; \
    cd /opt/runner; \
    clang-8 -c criterion-hooks.c -Wall -Wextra;

WORKDIR /workspace
USER codewarrior
