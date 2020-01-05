# ArchLinux image with MinGW toolchain

FROM softwareperonista/archlinux-mingw-w64-gtk3:latest
MAINTAINER tarmaciltur

# Update base system
RUN pacman -Syu --noconfirm --noprogressbar

# Update install packages needed
RUN pacman -Syu --noconfirm --noprogressbar sudo fuse git wget wine vala inkscape zip appstream-glib

# Install mingw-ldd
RUN curl https://raw.githubusercontent.com/xantares/mingw-ldd/master/mingw-ldd.py -o /usr/bin/mingw-ldd.py
RUN chmod -v +x /usr/bin/mingw-ldd.py

# Add devel user to build packages
RUN useradd -m -d /home/devel -u 1000 -U -G users,tty -s /bin/bash devel
RUN echo 'devel ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers
USER devel
ENV TERM dumb
ENV MAKEFLAGS "-j8"

# Install AUR helper
RUN git clone https://aur.archlinux.org/yay.git /tmp/yay \
    && cd /tmp/yay && makepkg -sfi --skippgpcheck --noconfirm

# Install Doctrina
RUN yay -S --noconfirm --nopgpfetch --mflags --skippgpcheck mingw-w64-doctrina
RUN yay -S --noconfirm --nopgpfetch --mflags --skippgpcheck doctrina

# Install python-pefile
RUN yay -S --noconfirm --nopgpfetch --mflags --skippgpcheck python-pefile

# Clean cache
RUN yay -Scc --noconfirm

# Change to root
USER root

