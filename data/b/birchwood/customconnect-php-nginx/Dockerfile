FROM webdevops/php-nginx-dev:7.3
ENV TZ=UTC

# Install imagick and mcrypt
RUN apt-get clean && apt-get update && apt-get -y install imagemagick libmagickwand-dev libmcrypt-dev && \
    pecl install imagick && \
    pecl install mcrypt-1.0.2 && \
    echo "extension=imagick.so" "\n" "extension=mcrypt.so" >> /usr/local/etc/php/conf.d/zz.ini && \
    rm -rf /var/lib/apt/lists/*

# Install newer ghostscript
RUN wget -qO- https://github.com/ArtifexSoftware/ghostpdl-downloads/releases/download/gs927/ghostscript-9.27-linux-x86_64.tgz \
    | tar xvz -C /tmp && mv /tmp/ghostscript-9.27-linux-x86_64/gs-927-linux-x86_64 /usr/bin/gs && chmod +x /usr/bin/gs && \
    rm -rf /tmp/ghostscript-9.27-linux-x86_64

EXPOSE 80
