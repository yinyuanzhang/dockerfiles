FROM oraclelinux:7-slim
LABEL maintainer "Bitnami <containers@bitnami.com>"
ENV IMAGE_OS=ol-7

COPY rootfs /

RUN install_packages openssl-libs postgresql-libs tar gzip oracle-epel-release-el7 && \
    yum-config-manager --enable ol7_developer_EPEL ol7_optional_latest && \
    yum upgrade -y 

ENV BITNAMI_IMAGE_VERSION=7-r555
