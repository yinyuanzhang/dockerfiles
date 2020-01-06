FROM archlinux/base

LABEL maintainer "Harpo Roeder <roederharpo@protonmail.ch>"

RUN pacman -Syu --noconfirm \
    && pacman -S --noconfirm autoconf automake cmake curl gcc git gmp libsigsegv libtool ncurses ninja openssl python ragel re2c meson pkgconf \
    && curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py \
    && python3 get-pip.py

RUN git clone https://github.com/urbit/urbit \
    && cd urbit \
    && ./scripts/bootstrap \
    && ./scripts/build \
    && ninja -C ./build/ meson-install

WORKDIR /ctx

VOLUME ["/ctx"]

EXPOSE 8080
EXPOSE 8443

ENTRYPOINT ["urbit"]
