FROM registry.fedoraproject.org/fedora-minimal:30

LABEL maintainer="SysAlpine <mail@sysalpine.com>"

ENV BAREOS_VERSION=18.2.6 \
    BAREOS_FD_PASSWORD=changeme \
    BAREOS_FD_NAME=localhost \
    BAREOS_FD_ADDRESS=0.0.0.0 \
    BAREOS_FD_PORT=9102 \
    BAREOS_FD_PKI_SIGNATURES=no \
    BAREOS_FD_PKI_ENCRYPTION=no \
    BAREOS_FD_PKI_CIPHER=aes128 \
    BAREOS_DIR_NAME=bareos-dir \
    BAREOS_DIR_ADDRESS=localhost \
    CONNECTION_FROM_CLIENT_TO_DIRECTOR=no \
    CONNECTION_FROM_DIRECTOR_TO_CLIENT=yes

COPY config/yum.repo /etc/yum.repos.d/bareos.repo

# Install Requirements
RUN microdnf --nodocs install hostname; microdnf clean all

# Install Bareos Filedaemon (Client)
RUN microdnf install --nodocs bareos-client-${BAREOS_VERSION}; microdnf clean all

# Install bareos configuration
COPY config/bareos-fd.conf /etc/bareos/bareos-fd.conf
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

EXPOSE 9102

ENTRYPOINT [ "/entrypoint.sh" ]
