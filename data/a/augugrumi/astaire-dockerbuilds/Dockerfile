FROM base/devel:latest

LABEL maintainer="poloniodavide@gmail.com"

RUN pacman -Sy --noconfirm \
    curl \
    git \
    sudo \
    cmake \
    boost && \
    useradd -d /home/builder builder && \
    mkdir -p /home/builder && \
    chown -R builder /home/builder && \
    echo 'builder ALL=(ALL) NOPASSWD: ALL' | sudo EDITOR='tee -a' visudo && \
    pacman -S --noconfirm \
    jdk8-openjdk \
    jsoncpp && \
    git clone https://aur.archlinux.org/pistache-git.git pistache && \
    cd pistache && \
    sed -i '/make test/d' PKGBUILD && \
    sed -i 's/-DPISTACHE_BUILD_TESTS=true/-DPISTACHE_BUILD_TESTS=false/g' PKGBUILD && \
    chown -R builder . && \
    su builder -c 'makepkg -isr --noconfirm' && \
    cd - && \
    rm -Rf pistache/ && \
    pacman -Rsc git --noconfirm

RUN mkdir -p /build/
VOLUME /build/
WORKDIR /build/

COPY builder.sh /usr/bin/builder
ENTRYPOINT ["builder"]

