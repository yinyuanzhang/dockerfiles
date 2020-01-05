# Archlinux with openconnect

FROM archlinux/base

# Whilst base pulls in quite a bit, most pkgs assume base is present without
# explicitly specifying so  its better to have it there
#
RUN pacman -Syu --noconfirm  && pacman -S --noconfirm base

RUN pacman -S --noconfirm openconnect

# Configure tun device needed for vpn
RUN mkdir -p /dev/net && \
    mknod /dev/net/tun c 10 200 && \
    chmod 600 /dev/net/tun

ENTRYPOINT ["openconnect"]
CMD ["--help"]
