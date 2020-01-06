FROM base/archlinux
ENV CONFIG_JSON1=none CONFIG_JSON2=none CMD=none UUID=51cbAC87-a373-3347-8169-33d4bbaeb857 CONFIG_JSON3=none PASS=none CERT_PEM=none KEY_PEM=none VER=3.19
RUN pacman -Syu --noconfirm && pacman -S bash unzip nano tor python2-gevent python2-msgpack python2-pyopenssl --noconfirm 
ADD inits /inits
RUN chmod +x /inits
RUN mkdir -p /lonp && chmod g+ws /lonp
WORKDIR /lonp
#ENTRYPOINT ["/sbin/inits"]
#Expose ports
#ENTRYPOINT /entrypoint.sh
CMD /inits
# EXPOSE 41022 13943
EXPOSE 8080
