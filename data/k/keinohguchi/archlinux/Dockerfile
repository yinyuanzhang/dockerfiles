# SPDX-License-Identifier: GPL-2.0
FROM archlinux/base
MAINTAINER Kei Nohguchi <kei@nohguchi.com>
# For Linux kernel compilation
RUN pacman -Sy --noconfirm gcc make bc bison flex gawk grep
# For BPF/XDP object compilation
RUN pacman -S --noconfirm clang llvm
# For CircleCI workspace
RUN pacman -S --noconfirm tar git openssh
CMD sh
