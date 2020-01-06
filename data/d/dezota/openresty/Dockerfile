FROM base/archlinux

MAINTAINER "Brian Holman" <bholman@dezota.com>

COPY mirrorlist /etc/pacman.d/mirrorlist 

RUN pacman -Syu --noconfirm && \
    pacman --noconfirm -S wget

RUN wget -O openresty-with-extras-1.13.6.1-1-x86_64.pkg.tar.xz  "https://github.com/Dezota/ArchLinuxPackages/raw/master/packages/openresty-with-extras-1.13.6.1-1-x86_64.pkg.tar.xz" && \
    pacman --noconfirm -U openresty-with-extras-1.13.6.1-1-x86_64.pkg.tar.xz && \
    rm openresty-with-extras-1.13.6.1-1-x86_64.pkg.tar.xz

EXPOSE 80

STOPSIGNAL SIGTERM

CMD ["/opt/openresty/nginx/sbin/nginx", "-g", "daemon off;"]


