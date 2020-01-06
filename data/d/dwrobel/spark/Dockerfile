FROM docker.io/fedora:29

LABEL maintainer="dwrobel@ertelnet.rybnik.pl" description="Base Docker image for building/running Spark (aka pxscene) within Docker"

ENV LC_ALL=en_US.UTF-8 \
    LANG=en_US.UTF-8 \
    LANGUAGE=en_US.UTF-8

RUN dnf install -y dnf-plugins-core

RUN dnf copr -y enable dwrobel/node-shared

# Equivalent of @Buildsystem building group + Spark dependencies + testunit dependencies (for glut and wayland backends) + everything you need to use Sanitizers (for both gcc and clang)
RUN dnf install -y \
    make diffutils unzip bash gawk which patch grep fedora-release info shadow-utils sed redhat-rpm-config tar rpm-build findutils util-linux gzip xz cpio coreutils-single bzip2 \
    git node8-shared-devel node-shared-devel procps-ng gdb quilt gcc-c++ libasan libtsan hostname gawk freeglut-devel glew-devel libgcrypt-devel bzip2-devel autoconf libtool cmake xorg-x11-drv-libinput-devel libcurl-devel libssh2-devel gnutls-devel libjpeg-turbo-devel turbojpeg-devel libpng-devel freetype-devel wayland-devel mesa-libEGL-devel mesa-libGLES-devel mesa-libwayland-egl-devel libuuid-devel \
    clang clang-analyzer sudo ccache weston mesa-dri-drivers xorg-x11-server-Xvfb expect v8-devel
RUN dnf debuginfo-install -y node-shared

RUN echo >/etc/sudoers.d/wheel-no-passwd '%wheel	ALL=(ALL)	NOPASSWD: ALL'

RUN dnf update -y

RUN dnf clean all
