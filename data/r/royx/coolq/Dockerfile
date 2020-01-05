FROM ubuntu:xenial

ENV LANGUAGE=zh_CN.UTF-8 \
    LC_ALL=zh_CN.UTF-8 \
    LANG=zh_CN.UTF-8 \
    DEBIAN_FRONTEND=noninteractive \
    DISPLAY=:0.0 \
    DISPLAY_WIDTH=1024 \
    DISPLAY_HEIGHT=768 \
    WINEPREFIX=/root/.wine32 \
    WINEARCH=win32 \
    VNC_PASSWORD=123456

RUN apt-get update \
        && apt-get install -y --no-install-recommends \
                ca-certificates \
                locales \
                socat \
                supervisor \
                x11vnc \
                xvfb \
        && locale-gen "zh_CN.UTF-8" \
        && dpkg-reconfigure locales \
        && echo "deb http://ppa.launchpad.net/ubuntu-wine/ppa/ubuntu xenial main" \
                > /etc/apt/sources.list.d/wine.list \
        && echo "deb-src http://ppa.launchpad.net/ubuntu-wine/ppa/ubuntu xenial main" \
                >> /etc/apt/sources.list.d/wine.list \
        && apt-key adv --keyserver keyserver.ubuntu.com --recv-keys F9CB8DB0 \
        && dpkg --add-architecture i386 \
        && apt-get update \
        && apt-get install -y --no-install-recommends \
                wine1.8 \
        && rm -rf /var/lib/apt/lists/*

RUN apt-get update \
        && apt-get install -y --no-install-recommends \
                cabextract \
                wget \
                unzip \
        && wget -O /usr/bin/winetricks https://raw.githubusercontent.com/Winetricks/winetricks/master/src/winetricks \
        && chmod +x /usr/bin/winetricks \
        && winetricks winhttp msscript cjkfonts \
        && cd /tmp \
        && wget http://dlsec.cqp.me/cqa-tuling -O CQA-tuling.zip \
        && unzip CQA-tuling.zip \
        && mv ./*Air /root/CoolQ \
        && wget -O /root/CoolQ/app/io.github.richardchien.coolqhttpapi.cpk https://github.com/richardchien/coolq-http-api/releases/download/v1.1.2/io.github.richardchien.coolqhttpapi.cpk \
        && apt-get remove -y --purge \
                cabextract \
                wget \
                unzip \
        && rm -rf /root/.cache /tmp/* /var/lib/apt/lists/*

COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

VOLUME /root/CoolQ/conf \
       /root/CoolQ/app/io.github.richardchien.coolqhttpapi

EXPOSE 5700 8080

CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/supervisord.conf"]
