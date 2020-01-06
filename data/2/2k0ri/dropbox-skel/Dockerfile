FROM ubuntu:latest
MAINTAINER Kei Kori <esc13245@gmail.com>

ENV DEBIAN_FRONTEND=noninteractive \
    LANGUAGE=ja_JP.UTF-8 \
    LANG=ja_JP.UTF-8 \
    LC_ALL=ja_JP.UTF-8
RUN apt-get update && \
    apt-get -o Dpkg::Options::="--force-confnew" --force-yes -fuy dist-upgrade && \
    apt-get install -y curl python-software-properties language-pack-ja && \
    locale-gen ja_JP.UTF-8 && \
    curl -L "https://www.dropbox.com/download?plat=lnx.x86_64" | tar xzf - && \
    curl -Lo /usr/bin/dropbox "https://www.dropbox.com/download?dl=packages/dropbox.py" && \
    chmod +x /usr/bin/dropbox && \
    apt-get remove --purge -y curl; apt-get -y autoremove; apt-get clean && \
    rm -rf /tmp/* /var/tmp/* /var/cache/apt/archives/* /var/lib/apt/lists/*

EXPOSE 17500

VOLUME ["/root/Dropbox"]

CMD /.dropbox-dist/dropboxd
