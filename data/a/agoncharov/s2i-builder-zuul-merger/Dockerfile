# s2i-zuul-zookeeper
FROM registry.fedoraproject.org/f28/s2i-base

LABEL maintainer="Artem Goncharov <artem.goncharov@gmail.com>"

ENV BUILDER_VERSION 0.1

ENV PYTHON_VERSION=3.6 \
    PATH=$HOME/.local/bin/:$PATH \
    PYTHONUNBUFFERED=1 \
    PYTHONIOENCODING=UTF-8 \
    LC_ALL=en_US.UTF-8 \
    LANG=en_US.UTF-8 \
    PIP_NO_CACHE_DIR=off

ENV NAME=python3 \
    VERSION=0 \
    RELEASE=1 \
    ARCH=x86_64

LABEL io.k8s.description="Platform for building Zuul Merger" \
      io.k8s.display-name="Builder Zuul Merger F28" \
      io.openshift.expose-services="" \
      io.openshift.tags="builder,zuul,merger,0.1.0"

# TODO: Install required packages here: required for pip install
RUN INSTALL_PKGS="python3 python3-devel python3-setuptools python3-pip \
    python3-virtualenv re2-devel nss_wrapper" && \
    dnf -y --setopt=tsflags=nodocs install $INSTALL_PKGS && \
    rpm -V $INSTALL_PKGS && \
    dnf -y clean all --enablerepo='*'

# TODO: Copy the S2I scripts to $STI_SCRIPTS_PATH, since s2i-base image
# sets io.openshift.s2i.scripts-url label that way, or update that label
COPY ./s2i/bin/ $STI_SCRIPTS_PATH

# Copy extra files to the image.
COPY ./root/ /

# - Create a Python virtual environment for use by any application to avoid
#   potential conflicts with Python packages preinstalled in the main Python
#   installation.
# - In order to drop the root user, we have to make some directories world
#   writable as OpenShift default security model is to run the container
#   under random UID. Zuul directories are created with 775 to give root group rwx
RUN virtualenv-$PYTHON_VERSION ${APP_ROOT} && \
    mkdir -m 775 -p /etc/zuul /var/run/zuul /var/lib/zuul /var/log/zuul && \
    chown -R 1001:0 /etc/zuul /var/run/zuul /var/lib/zuul /var/log/zuul && \
    chown -R 1001:0 ${APP_ROOT} && \
    fix-permissions ${APP_ROOT} -P

# This default user is created in the s2i-base image
USER 1001

# Set the default CMD to print the usage of the language image.
CMD $STI_SCRIPTS_PATH/usage
