FROM patricol/gui_base:arch

RUN update \
 && addpackages \
    filezilla \
 && clearcache \
 && ln -sf /config/ ~/.config/filezilla \
 && echo "sudo chown user:users /config" >> /scripts/startapp \
 && echo "exec filezilla" >> /scripts/startapp

VOLUME /config
VOLUME /local_files
