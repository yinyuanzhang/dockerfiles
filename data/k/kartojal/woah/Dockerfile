# Docker image that installs all Grin dependencies

# Author: David Canillas Racero
FROM nvidia/cuda:10.0-cudnn7-devel 

ENV RUSTUP_HOME=/usr/local/rustup \
    CARGO_HOME=/usr/local/cargo \
    PATH=/usr/local/cargo/bin:$PATH \
    RUST_VERSION=1.32.0

# Install dependencies

RUN apt update
RUN apt install -y wget dpkg-dev git build-essential vim curl zlib1g-dev libncurses5-dev libncursesw5-dev zlib1g-dev pkg-config libssl-dev cmake screen


# Install official grin miner
WORKDIR /root
RUN git clone https://github.com/mimblewimble/grin-miner.git

WORKDIR /root/grin-miner

# Init repo
RUN git submodule update --init

# Allow to compile CUDA drivers
RUN sed -i '38s/^/#/' Cargo.toml
RUN sed -i '40s/^#//' Cargo.toml

# Build RUST Package
RUN set -eux; \
    dpkgArch="$(dpkg --print-architecture)"; \
    case "${dpkgArch##*-}" in \
        amd64) rustArch='x86_64-unknown-linux-gnu'; rustupSha256='2d4ddf4e53915a23dda722608ed24e5c3f29ea1688da55aa4e98765fc6223f71' ;; \
        armhf) rustArch='armv7-unknown-linux-gnueabihf'; rustupSha256='be85f50dc70ee239c5bb6acb60080797841a1e7c45fbf6bae15d6bd4b37ce0e5' ;; \
        arm64) rustArch='aarch64-unknown-linux-gnu'; rustupSha256='454f00a86be75ab070149bac1f541a7b39e5d3383d6da96ad2b929867ed40167' ;; \
        i386) rustArch='i686-unknown-linux-gnu'; rustupSha256='179e3b39f11037a708874e750081f7c0d3e1a6a4c431c2ecee2295acc7b696af' ;; \
        *) echo >&2 "unsupported architecture: ${dpkgArch}"; exit 1 ;; \
    esac; \
    url="https://static.rust-lang.org/rustup/archive/1.16.0/${rustArch}/rustup-init"; \
    wget "$url"; \
    echo "${rustupSha256} *rustup-init" | sha256sum -c -; \
    chmod +x rustup-init; \
    ./rustup-init -y --no-modify-path --default-toolchain $RUST_VERSION; \
    rm rustup-init; \
    chmod -R a+w $RUSTUP_HOME $CARGO_HOME; \
    cargo build;

# Comment line 40 to 52 at grin-miner.toml (Auth)
RUN sed -i '40,52s/^/#/' grin-miner.toml

# Comment line 79 to 82 at grin-miner.toml (GPU config)
RUN sed -i '79,82s/^/#/' grin-miner.toml
