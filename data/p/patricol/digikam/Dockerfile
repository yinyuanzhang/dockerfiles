FROM patricol/gui_base:arch

RUN update \
 && addpackages \
    digikam qt5ct \
    qt5-imageformats \
 && clearcache \ 
 && echo "sudo chown user:users /config /data" >> /scripts/startapp \
 && echo "mkdir -p /config/share" >> /scripts/startapp \
 && echo "exec digikam" >> /scripts/startapp \
 && sudo mkdir -p /config /config/share /home/user/.local \
 && sudo ln -s /config/share/ /home/user/.local/share \
 && sudo ln -s /config/digikamrc /home/user/.config/digikamrc \
 && sudo ln -s /config/digikam_tagsmanagerrc /home/user/.config/digikam_tagsmanagerrc \
 && sudo ln -s /config/showfotorc /home/user/.config/showfotorc \
 && sudo chown -R user:users /home/user/.local

VOLUME /config
VOLUME /data
