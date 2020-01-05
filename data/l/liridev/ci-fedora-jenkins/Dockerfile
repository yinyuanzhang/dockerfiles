FROM liridev/ci-fedora:31
MAINTAINER Pier Luigi Fiorini <pierluigi.fiorini@gmail.com>
RUN set -ex && \
    groupadd -g 1002 jenkins && \
    useradd -c "Jenkins" -u 1001 -g 1002 -m -G wheel jenkins && \
    echo "%wheel ALL=(ALL) NOPASSWD: ALL" >/etc/sudoers.d/wheel
USER jenkins
