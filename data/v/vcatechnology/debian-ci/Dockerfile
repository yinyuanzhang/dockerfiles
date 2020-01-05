FROM vcatechnology/debian:8
MAINTAINER VCA Technology <developers@vcatechnology.com>

# Build-time metadata as defined at http://label-schema.org
ARG PROJECT_NAME
ARG BUILD_DATE
ARG VCS_REF
ARG VERSION
LABEL org.label-schema.build-date=$BUILD_DATE \
      org.label-schema.name="$PROJECT_NAME" \
      org.label-schema.description="An up-to-date Debian image with basic tool chain packages" \
      org.label-schema.url="https://www.debian.org/" \
      org.label-schema.vcs-ref=$VCS_REF \
      org.label-schema.vcs-url="https://github.com/vcatechnology/docker-debian-ci" \
      org.label-schema.vendor="VCA Technology" \
      org.label-schema.version=$VERSION \
      org.label-schema.license=MIT \
      org.label-schema.schema-version="1.0"

# Make sure that we generate the timestamp file for APT updates
RUN echo 'APT::Update::Post-Invoke-Success {"touch /var/lib/apt/periodic/update-success-stamp 2>/dev/null || true";};' > /etc/apt/apt.conf.d/15update-stamp

# Install useful packages
RUN vca-install-package \
  python \
  git \
  openssh-client \
  sudo \
  rsync

# grab the VCA CI Scripts
RUN vca-install-package wget xz-utils && \
  wget -q https://tool-chain.vcatechnology.com/release/vca-tool-chain-ci-scripts-latest.tar.xz && \
  tar -Jxf vca-tool-chain-ci-scripts-latest.tar.xz -C / && \
  rm vca-tool-chain-ci-scripts-latest.tar.xz && \
  vca-uninstall-package wget xz-utils

# create a build-server user with sudo permissions & no password
RUN useradd -ms /bin/bash build-server && \
    echo "build-server ALL=(root) NOPASSWD:ALL" | tee -a /etc/sudoers.d/build-server && \
    chmod 0440 /etc/sudoers.d/build-server

# Set the build-server user as default
RUN mkdir /mnt/builds
WORKDIR /mnt/builds
RUN chown build-server:build-server /mnt/builds
USER build-server
