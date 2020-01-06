FROM fedora:29

MAINTAINER korolev.srg@gmail.com

RUN dnf install -y \
  flatpak flatpak-builder wget git bzip2 elfutils make ostree -y && \
  dnf clean all
