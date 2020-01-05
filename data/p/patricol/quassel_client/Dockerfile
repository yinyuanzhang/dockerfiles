FROM patricol/gui_base:arch

RUN update \
 && addpackages \
    quassel-client-small qt5ct \
    breeze-icons \
 && clearcache \
 && ln -sf /config/ ~/.config/quassel-irc.org \
 && echo "sudo chown user:users /config" >> /scripts/startapp \
 && echo "exec quasselclient" >> /scripts/startapp

VOLUME /config
