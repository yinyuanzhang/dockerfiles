FROM ubuntu:bionic as build

ARG VERSION=0.5.31

ENV ROOTFS /build/rootfs
ENV DEBIAN_FRONTEND noninteractive

# Build pre-requisites
RUN bash -c 'mkdir -p ${BUILD_DEBS} ${ROOTFS}/{usr/local/bin}'

RUN apt-get update \
      && apt-get install -yq python3-pip \
      && pip3 install --upgrade --root ${ROOTFS} nuitka==${VERSION}

COPY entrypoint.sh ${ROOTFS}/usr/local/bin/entrypoint.sh
RUN chmod +x ${ROOTFS}/usr/local/bin/entrypoint.sh

FROM actions/python:3.6.5-2
LABEL maintainer = "ilja+docker@bobkevic.com"

ARG ROOTFS=/build/rootfs

ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

COPY --from=build ${ROOTFS} /

ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]