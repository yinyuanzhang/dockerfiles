FROM fedora:latest
MAINTAINER Giuseppe Scrivano <gscrivan@redhat.com>

LABEL Name ostreetests
LABEL Release 1.0
LABEL Version 1.0

ADD run.sh /run.sh
RUN dnf install -y 'dnf-command(builddep)' redhat-rpm-config bison rsync gcc git autoconf automake which gtk-doc libtool libcap-devel gnome-desktop-testing attr parallel gjs fuse-libs fuse-devel && dnf builddep -y ostree && dnf clean all -y

CMD /run.sh
