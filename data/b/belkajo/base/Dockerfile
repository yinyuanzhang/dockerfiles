FROM fedora:30
LABEL version="2.0"
LABEL name="base"

RUN dnf --setopt=install_weak_deps=False --best -y  install  \
    http://rpms.remirepo.net/fedora/remi-release-30.rpm \
    dnf-plugins-core && \
  dnf config-manager --set-enabled remi && \
  rpm --import /etc/pki/rpm-gpg/RPM-GPG-KEY-remi-30 && \
  dnf --setopt=install_weak_deps=False --best -y update && \
  dnf --setopt=install_weak_deps=False --best -y install  \
    git \
    iputils \
    mcrypt \
    mhash \
    openssl \
    p7zip \
    patch \
    unzip \
    which \
    zip \
    bind-utils \
    mariadb \
    procps \
    rsync \
    lsof && \
  dnf clean all

ENV USER=webuser

COPY start.sh /usr/local/bin/start.sh
RUN chmod +x /usr/local/bin/start.sh
ENTRYPOINT [ "/usr/local/bin/start.sh" ]
