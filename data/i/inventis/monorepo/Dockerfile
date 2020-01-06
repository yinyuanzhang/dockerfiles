FROM inventis/composer:7.2

RUN echo "deb http://ftp.de.debian.org/debian testing main" >> /etc/apt/sources.list \
    && apt-get update \
    && apt-get -t testing install -y python3.6 \
    && ln -s /usr/bin/python3.6 /usr/bin/python3 \
    && echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen \
    && locale-gen \
    && export LANG=en_US.UTF-8
