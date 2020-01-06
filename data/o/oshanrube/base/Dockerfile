FROM fedora:23

# This image is the base image for all OpenShift v3 language Docker images.
MAINTAINER Oshan Rube <oshanrube@gmail.com>

# Location of the STI scripts inside the image
#
LABEL io.openshift.s2i.scripts-url=image:///usr/libexec/s2i

# DEPRECATED: This label will be kept here for backward compatibility
LABEL io.s2i.scripts-url=image:///usr/libexec/s2i

# Deprecated. Use above LABEL instead, because this will be removed in future versions.
ENV STI_SCRIPTS_URL=image:///usr/libexec/s2i

# Path to be used in other layers to place s2i scripts into
ENV STI_SCRIPTS_PATH=/usr/libexec/s2i

# The $HOME is not set by default, but some applications needs this variable
ENV HOME=/opt/app-root/src \
    PATH=/opt/app-root/src/bin:/opt/app-root/bin:$PATH

# When bash is started non-interactively, to run a shell script, for example it
# looks for this variable and source the content of this file. This will enable
# the SCL for all scripts without need to do 'scl enable'.
COPY contrib/scl_enable /opt/app-root/etc/scl_enable
ENV BASH_ENV=/opt/app-root/etc/scl_enable \
    ENV=/opt/app-root/etc/scl_enable \
    PROMPT_COMMAND=". /opt/app-root/etc/scl_enable"

# This is the list of basic dependencies that all language Docker image can
# consume.
# Also setup the 'openshift' user that is used for the build execution and for the
# application runtime execution.
# TODO: Use better UID and GID values
RUN dnf install -y --setopt=tsflags=nodocs \
  autoconf automake bsdtar findutils gcc-c++ gdb gettext git libcurl-devel libxml2-devel libxslt-devel \
  lsof make openssl-devel patch postgresql-devel procps-ng scl-utils sqlite-devel tar unzip wget which yum-utils zlib-devel \
  libxml2 libarchive glibc sqlite rpm && \
  dnf clean all -y && \
  mkdir -p ${HOME} && \
  useradd -u 1001 -r -g 0 -d ${HOME} -s /sbin/nologin \
      -c "Default Application User" default && \
  chown -R 1001:0 /opt/app-root

# Create directory where the image STI scripts will be located
# Install the base-usage script with base image usage informations
COPY bin/base-usage /usr/bin/base-usage

# Use entrypoint so path is correctly adjusted already at the time the command
# is searching, so something like docker run IMG python runs binary from SCL
COPY bin/container-entrypoint /usr/bin/container-entrypoint

# Add script to fix directory permissions
COPY bin/fix-permissions /usr/bin/fix-permissions

# Directory with the sources is set as the working directory so all STI scripts
# can execute relative to this path
WORKDIR ${HOME}

ENTRYPOINT ["container-entrypoint"]
CMD ["base-usage"]
