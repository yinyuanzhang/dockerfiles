FROM debian:stretch

RUN apt-get update \
    && apt-get install -y \
        curl \
        git \
        gnupg \
        lua5.3 \
        lua5.3-dev \
        luarocks \
        make \
        python3 \
    && echo "deb http://apt.llvm.org/stretch/ llvm-toolchain-stretch-7 main" >> /etc/apt/sources.list \
    && echo "deb-src http://apt.llvm.org/stretch/ llvm-toolchain-stretch-7 main" >> /etc/apt/sources.list \
    && curl --silent https://apt.llvm.org/llvm-snapshot.gpg.key | apt-key add - \
    && apt-get update \
    && apt-get install -y \
        clang-format-7 \
        libclang-7-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    && git config --global core.quotepath false

RUN luarocks install ldoc \
    && luarocks install luacheck

RUN curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y
