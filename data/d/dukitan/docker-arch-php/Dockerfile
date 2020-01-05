FROM base/archlinux
MAINTAINER David Ferreira <davidferreira.fz@gmail.com>

RUN pacman -Syu --noconfirm 
RUN pacman -S php composer lftp sshpass --noconfirm
RUN pacman -Scc --noconfirm
