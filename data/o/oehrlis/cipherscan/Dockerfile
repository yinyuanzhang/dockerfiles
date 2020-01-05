# ----------------------------------------------------------------------
# Trivadis AG, Infrastructure Managed Services
# Saegereistrasse 29, 8152 Glattbrugg, Switzerland
# ----------------------------------------------------------------------
# Name.......: Dockerfile
# Author.....: Stefan Oehrli (oes) stefan.oehrli@trivadis.com
# Editor.....: Stefan Oehrli
# Date.......: 2018.03.19
# Revision...: 1.0
# Purpose....: Dockerfile to build a cipherscan image
# Notes......: --
# Reference..: --
# License....: Licensed under the Universal Permissive License v 1.0 as
#              shown at http://oss.oracle.com/licenses/upl.
# ----------------------------------------------------------------------
# Modified...:
# see git revision history for more information on changes/updates
# ----------------------------------------------------------------------

# Pull base image
# ----------------------------------------------------------------------
FROM alpine

# Maintainer
# ----------------------------------------------------------------------
LABEL maintainer="stefan.oehrli@trivadis.com"

# Environment variables required for this build (do NOT change)
# -------------------------------------------------------------
ENV DOWNLOAD="/tmp/download" \
    INSTALL_DIR="/opt" \
    CIPHERSCAN_DIR="/opt/cipherscan" \
    PATH="${PATH}:/opt/cipherscan"

# RUN as user root
# ----------------------------------------------------------------------
# - install a few packages
# - create folders
# - download cipherscan from git
# - unpack cipherscan
# - run cscan.sh on google.com to implicit download tlslite and ecdsa
# - remove git and apk cache
# -----------------------------------------------------------------
RUN apk --update add curl bash python py2-six util-linux gcompat git && \
    mkdir -p ${DOWNLOAD} ${INSTALL_DIR} && \
    curl -f https://codeload.github.com/mozilla/cipherscan/zip/master -o ${DOWNLOAD}/master.zip  && \
    unzip ${DOWNLOAD}/master.zip -d ${INSTALL_DIR} && \
    ls -al ${INSTALL_DIR} && \
    mv ${INSTALL_DIR}/cipherscan-master ${CIPHERSCAN_DIR} && \
    ${CIPHERSCAN_DIR}/cscan.sh google.com && \
    rm ${CIPHERSCAN_DIR}/ecdsa && \
    mv ${CIPHERSCAN_DIR}/.python-ecdsa/src/ecdsa ${CIPHERSCAN_DIR}/ecdsa && \
    rm ${CIPHERSCAN_DIR}/tlslite && \
    mv ${CIPHERSCAN_DIR}/.tlslite-ng/tlslite ${CIPHERSCAN_DIR}/tlslite && \
    apk del git curl && \
    rm -rf /var/cache/apk/* \
        ${DOWNLOAD}/master.zip \
        ${CIPHERSCAN_DIR}/top1m \
        ${CIPHERSCAN_DIR}/openssl-darwin64 \
        ${CIPHERSCAN_DIR}/.gitignore \
        ${CIPHERSCAN_DIR}/.travis.yml \
        ${CIPHERSCAN_DIR}/.python-ecdsa \
        ${CIPHERSCAN_DIR}/.tlslite-ng 

# set workding directory
WORKDIR ${CIPHERSCAN_DIR}

# Define default command to start OUD instance
CMD ["cipherscan", "--help"]