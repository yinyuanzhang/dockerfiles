FROM archlinux/base

MAINTAINER saye@sknss.net

RUN pacman -Sy && \
  pacman -S archlinux-keyring --noconfirm && \
  pacman -S pacman --noconfirm && \
  pacman-db-upgrade && \
  pacman -Su --noconfirm && \
  pacman -S git openssh docker make sed awk gzip grep curl vim tree iproute2 inetutils jq --noconfirm --needed && \
  locale-gen en_US.UTF-8 && \
  pacman -Scc --noconfirm

ENV LANG=en_US.UTF-8
CMD ["/usr/bin/bash"]
