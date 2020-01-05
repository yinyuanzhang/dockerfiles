FROM mhart/alpine-node:8.11

ARG GHR_VERSION=v0.12.0
ARG VARIANT=linux_amd64
ARG URL=https://github.com/tcnksm/ghr/releases/download/${GHR_VERSION}/ghr_${GHR_VERSION}_${VARIANT}.tar.gz

RUN apk -v --update add \
  python \
  py-pip \
  groff \
  less \
  mailcap \
  tar \
  gzip \
  ca-certificates \
  git \
  docker \
  openrc \
  wget \
  && \
  pip install --upgrade awscli && \
  # Prepare for download context directory
  mkdir /tmp/ghr_download && \
  cd /tmp/ghr_download && \
  # Download the tarball from Github
  wget ${URL} -O - | tar xz && \
  # Copy the binary and change owner
  cp ghr_${GHR_VERSION}_${VARIANT}/ghr /usr/local/bin/ghr && \
  chown root:root /usr/local/bin/ghr && \
  # Remove the download context directory
  rm -rf /tmp/ghr_download && \
  apk -v --purge del py-pip && \
  rm /var/cache/apk/*