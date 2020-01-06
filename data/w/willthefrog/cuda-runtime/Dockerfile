FROM archlinux/base
ARG cuda=cuda9
ENV NVIDIA_VISIBLE_DEVICES all
ENV NVIDIA_DRIVER_CAPABILITIES compute,utility
COPY makepkg.conf /etc/makepkg.conf
COPY pacman.conf /pacman.conf
RUN pacman -Sy --noconfirm --config /pacman.conf ${cuda}-runtime ; \
        rm /pacman.conf ; pacman -Scc --noconfirm ; rm /var/lib/pacman/sync/*
