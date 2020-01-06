# Container definition
FROM alpine:3.10

# Container configuration variables
ARG CONDA_VERSION_MAJOR=4
ARG CONDA_VERSION_MINOR=7
ARG CONDA_VERSION_BUILD=10
ARG CONDA_CHECKSUM="1c945f2b3335c7b2b15130b1b2dc5cf4"
ARG GLIBC_REPO=https://github.com/sgerrand/alpine-pkg-glibc
ARG GLIBC_VERSION=2.28-r0

# Container environment variables
ENV CONDA_HOME=/usr/local/miniconda \
    LANG=C.UTF-8

# Do all in one step
RUN apk -U upgrade && \
    apk add libstdc++ curl ca-certificates bash && \
    for pkg in glibc-${GLIBC_VERSION} glibc-bin-${GLIBC_VERSION} glibc-i18n-${GLIBC_VERSION}; do curl -sSL ${GLIBC_REPO}/releases/download/${GLIBC_VERSION}/${pkg}.apk -o /tmp/${pkg}.apk; done && \
    apk add --allow-untrusted /tmp/*.apk && \
    rm -v /tmp/*.apk && \
    ( /usr/glibc-compat/bin/localedef --force --quiet --inputfile POSIX --charmap UTF-8 C.UTF-8 || true ) && \
    echo "export LANG=C.UTF-8" > /etc/profile.d/locale.sh && \
    /usr/glibc-compat/sbin/ldconfig /lib /usr/glibc-compat/lib && \
    \
    mkdir -p "${CONDA_HOME}" && \
    curl -o /tmp/miniconda.sh "https://repo.continuum.io/miniconda/Miniconda3-${CONDA_VERSION_MAJOR}.${CONDA_VERSION_MINOR}.${CONDA_VERSION_BUILD}-Linux-x86_64.sh" && \
    echo "${CONDA_CHECKSUM}  /tmp/miniconda.sh" | md5sum -c && \
    bash /tmp/miniconda.sh -f -b -p "${CONDA_HOME}" && \
    for exec in `ls ${CONDA_HOME}/bin`; do ln -s ${CONDA_HOME}/bin/${exec} /usr/local/bin/${exec}; done && \
    rm /tmp/miniconda.sh && \
    \
    conda config --set auto_update_conda False && \
    rm -r "${CONDA_HOME}/pkgs/" && \
    \
    apk del curl glibc-i18n && \
    echo 'hosts: files mdns4_minimal [NOTFOUND=return] dns mdns4' >> /etc/nsswitch.conf
