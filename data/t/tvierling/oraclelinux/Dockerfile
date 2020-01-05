# 20190910

FROM oraclelinux:8

MAINTAINER Todd Vierling <tv@duh.org>

RUN dnf update -y && \
    dnf install -y man sudo emacs-nox nano vim glibc-devel.i686 \
                   elfutils-libelf-devel glib2-devel elfutils-devel bc && \
    dnf group install -y "Development Tools" && \
    dnf clean all && rm -rf /var/cache/dnf/*
