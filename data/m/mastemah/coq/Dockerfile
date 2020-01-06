# Coq theorem prover
FROM archlinux/base

RUN    pacman-key --init \
    && pacman-key --populate archlinux \
    && pacman --noconfirm -Syu \
    && pacman --noconfirm -S base-devel coq \
    && rm -f \
       /var/cache/pacman/pkg/*

WORKDIR /coq