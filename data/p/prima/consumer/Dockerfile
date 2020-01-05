FROM prima/php:7.2.24-4

ENV GHOSTSCRIPT_SHA256=8341407ed12434bb248ecee081528f68429664d85c9bfbce883459dcbdd852bb

RUN echo "deb-src http://deb.debian.org/debian stretch main" >> /etc/apt/sources.list && \
    echo "deb-src http://security.debian.org stretch/updates main" >> /etc/apt/sources.list && \
    apt-get update && \
    apt-get install -y redis-tools build-essential curl && \
    apt-get -y build-dep imagemagick && \
    curl -L -o /opt/ghostscript.tgz https://github.com/ArtifexSoftware/ghostpdl-downloads/releases/download/gs922/ghostscript-9.22-linux-x86_64.tgz && \
    cd /opt && \
    echo "${GHOSTSCRIPT_SHA256} ghostscript.tgz" | sha256sum -c - && \
    tar xzf ghostscript.tgz && \
    rm ghostscript.tgz && \
    cd /opt/ghostscript-9.22-linux-x86_64 && \
    mv gs-922-linux-x86_64 /usr/bin/gs && \
    chmod +x /usr/bin/gs && \
    curl -L -o /opt/imagemagick.tar.gz https://www.imagemagick.org/download/releases/ImageMagick-7.0.9-2.tar.gz && \
    cd /opt && \
    tar xzf imagemagick.tar.gz && \
    rm imagemagick.tar.gz && \
    cd /opt/ImageMagick-7.0.9-2 && \
    ./configure && \
    make -j $(nproc) && \
    make install && \
    mkdir -p /usr/share/man/man1 && \
    apt-get install -y pdftk && \
    apt-get install -y xz-utils libxext6 libfontconfig1 libxrender-dev && \
    apt-get install -y xfonts-base xfonts-75dpi xfonts-utils libfontenc1 xfonts-encodings && \
    curl -L -o /opt/wkhtmltox_0.12.5-1.stretch_amd64.deb https://github.com/wkhtmltopdf/wkhtmltopdf/releases/download/0.12.5/wkhtmltox_0.12.5-1.stretch_amd64.deb && \
    dpkg -i /opt/wkhtmltox_0.12.5-1.stretch_amd64.deb && \
    apt-get install -y python python-pip unzip rsync && \
    pip install supervisor --pre && \
    pip install --upgrade awscli && \
    aws configure set s3.signature_version s3v4 && \
    apt-get install -y bzip2 libfontconfig1 && \
    pecl install imagick && \
    echo "extension=imagick.so" > /usr/local/etc/php/conf.d/docker-php-ext-imagick.ini && \
    apt-get -y remove --purge xz-utils bzip2 build-essential python-pip && \
    apt-get install -y nginx && \
    rm /etc/nginx/sites-enabled/default && \
    rm -r /var/lib/apt/lists/* && \
    rm -rf /opt/ghostscript* /opt/ImageMagick* /opt/wkhtmltox* && \
    mkdir -p /var/log/prima && \
    gs --version && \
    convert --version && \
    wkhtmltopdf --version && \
    php -i | grep -i imagemagick && \
    supervisord --version

EXPOSE 9001

COPY files/fpm.d/* /usr/local/etc/fpm.d/
COPY files/entrypoint.sh /entrypoint.sh
COPY files/prima.ini /usr/local/etc/php/conf.d/prima.ini
COPY files/nginx/* /etc/nginx/sites-enabled/
# Temporary RCE mitigation (https://imagetragick.com/), upgrade imagemagick as soon as the proper fix is released
COPY files/policy.xml /etc/ImageMagick/policy.xml

ENV FPM_MAX_CHILDREN=5 \
    FPM_START_SERVERS=2 \
    FPM_MIN_SPARE_SERVERS=1 \
    FPM_MAX_SPARE_SERVERS=2 \
    PHP_MAX_EXECUTION_TIME=15 \
    NGINX_HTTP_HOST=localhost

CMD ["supervisord", "-n", "-c", "/etc/supervisord.conf"]
