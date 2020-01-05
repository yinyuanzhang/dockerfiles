FROM patricol/gui_base:arch

RUN update \
 && addpackages \
    freerdp \
    libvncserver \
    remmina \
 && clearcache \
 && ln -sf /config/ ~/.config/remmina \
 && echo "sudo chown user:users /config" >> /scripts/startapp \
 && echo "exec remmina" >> /scripts/startapp

VOLUME /config
