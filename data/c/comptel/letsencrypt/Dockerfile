FROM ubuntu:bionic

ENV DUMB_INIT_VERSION 1.2.1
ENV AZCOPY_VERSION 7.2.0
ENV SECRETARY_VERSION=0.10.1

COPY files/ /

WORKDIR /

# Set up certificates, base tools, dumb-init, install certbot/letsencrypt and azcopy.
RUN apt update && \
    apt --no-install-recommends install -y \
        certbot \
        gpg gpgv2 gpg-agent \
        curl \
        libunwind8 \
        libicu60 \
        libssl1.0.0 \
        wget rsync && \
    mv /tar-and-azure-upload.sh /usr/bin/tar-and-azure-upload.sh && \
    mv /post_cert.py /usr/bin/post_cert.py && \
    AZCOPY_VER="$(echo "${AZCOPY_VERSION}" | tr -s '.' '-')" && \
    wget -O /usr/bin/dumb-init https://github.com/Yelp/dumb-init/releases/download/v${DUMB_INIT_VERSION}/dumb-init_${DUMB_INIT_VERSION}_amd64 && \
    wget -O /usr/bin/secretary https://github.com/meltwater/secretary/releases/download/${SECRETARY_VERSION}/secretary-Linux-x86_64 && \
    chmod +x \
        /letsencrypt.sh \
        /docker-entrypoint.sh \
        /usr/bin/dumb-init \
        /usr/bin/secretary \
        /usr/bin/tar-and-azure-upload.sh \
        /usr/bin/post_cert.py && \
    wget -O azcopy.tar.gz https://azcopy.azureedge.net/azcopy-${AZCOPY_VER}/azcopy_${AZCOPY_VERSION}-netcore_linux_x64.tar.gz && \
    tar -xf azcopy.tar.gz && \
    ./install.sh && \
    rm -rf azcopy.tar.gz azcopy install.sh && \
    apt remove -y wget rsync && \
    apt autoremove -y && \
    rm -rf /var/lib/apt/lists/*

EXPOSE 80

ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["/letsencrypt.sh"]





