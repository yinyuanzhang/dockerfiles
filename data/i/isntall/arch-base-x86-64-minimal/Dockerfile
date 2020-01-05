FROM isntall/arch-base-x86_64:latest
MAINTAINER Archie Brentano <isntall.us@gmail.com>

RUN echo "Server = http://mirrors.cat.pdx.edu/archlinux/\$repo/os/\$arch" >> /etc/pacman.d/mirrorlist
RUN pacman-key --init && pacman-key --populate archlinux
RUN pacman -Syyu --noconfirm
RUN pacman -S --noconfirm wget rsync openssh vim
RUN pacman -Scc --noconfirm

