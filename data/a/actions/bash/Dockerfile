FROM ubuntu:bionic as build

ARG REQUIRED_PACKAGES="coreutils bash zlib1g libtinfo5 libselinux1"

ENV ROOTFS /build/rootfs
ENV BUILD_DEBS /build/debs
ENV DEBIAN_FRONTEND=noninteractive

# Build pre-requisites
RUN bash -c 'mkdir -p ${BUILD_DEBS} ${ROOTFS}/{bin,sbin,usr/share,usr/bin,usr/sbin,usr/lib,/usr/local/bin}'

# Fix permissions
RUN chown -Rv 100:root $BUILD_DEBS

# Install pre-requisites
RUN apt-get update \
        && apt-get -y install apt-utils locales

# UTF8 support
RUN echo "LC_ALL=en_US.UTF-8" > /etc/environment \
        && echo "en_US.UTF-8 UTF-8" > /etc/locale.gen \
        && echo "LANG=en_US.UTF-8" > /etc/locale.conf \
        && locale-gen en_US.UTF-8 \
        && cp -R /usr/lib/locale $ROOTFS/usr/lib/locale \
        && cp -R /usr/share/locale $ROOTFS/usr/share/locale \
        && cp -R /usr/share/locales $ROOTFS/usr/share/locales \
        && cp -R /usr/share/i18n $ROOTFS/usr/share/i18n

# CA certs
RUN apt-get install -y ca-certificates \
      && update-ca-certificates \
      && cp -r /etc/ssl $ROOTFS/etc \
      && cp -r /usr/share/ca-certificates $ROOTFS/usr/share

# Unpack required packges to rootfs
RUN cd ${BUILD_DEBS} \
  && for pkg in $REQUIRED_PACKAGES; do \
       apt-get download $pkg \
         && apt-cache depends --recurse --no-recommends --no-suggests --no-conflicts --no-breaks --no-replaces --no-enhances --no-pre-depends -i $pkg | grep '^[a-zA-Z0-9]' | xargs apt-get download ; \
     done
RUN if [ "x$(ls ${BUILD_DEBS}/)" = "x" ]; then \
      echo No required packages specified; \
    else \
      for pkg in ${BUILD_DEBS}/*.deb; do \
        echo Unpacking $pkg; \
        dpkg -x $pkg ${ROOTFS}; \
      done; \
    fi

RUN echo "root:x:0:0:root:/home:/bin/bash" > ${ROOTFS}/etc/passwd \
    && echo "root:x:0:" > ${ROOTFS}/etc/group

COPY entrypoint.sh ${ROOTFS}/usr/local/bin/entrypoint.sh
RUN chmod +x ${ROOTFS}/usr/local/bin/entrypoint.sh

FROM scratch
LABEL maintainer = "ilja+docker@bobkevic.com"

ARG ROOTFS=/build/rootfs

ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

COPY --from=build ${ROOTFS} /

ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]