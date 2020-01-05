FROM patricol/gui_base:arch

RUN update \
 && addpackages \
    calibre qt5ct \
    poppler \
 && clearcache \
 && ln -sf /config/ ~/.config/calibre \
 && echo "sudo chown user:users /config /library" >> /scripts/startapp \
 && echo "exec calibre" >> /scripts/startapp

EXPOSE 8081

VOLUME /config
VOLUME /library
