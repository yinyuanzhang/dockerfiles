FROM fedora:27
MAINTAINER Matthew Schick <matthew.schick@gmail.com>

ARG FEDVER=27

# Add rpmfusion repo, do package updates and installs
RUN dnf install -yq \
    http://download1.rpmfusion.org/free/fedora/rpmfusion-free-release-${FEDVER}.noarch.rpm \
    http://download1.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-${FEDVER}.noarch.rpm && \
    rpm --import /etc/pki/rpm-gpg/RPM-GPG-KEY-rpmfusion-free-fedora-27-primary && \
    rpm --import /etc/pki/rpm-gpg/RPM-GPG-KEY-rpmfusion-nonfree-fedora-27-primary && \
    dnf upgrade -yq && \
    dnf clean all
