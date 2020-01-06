FROM debian
MAINTAINER putty182
RUN DEBIAN_FRONTEND=noninteractive \
    apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y deluge-web
# Disable webui password: 
# https://gravemind.sh/blog/?p=511
# https://dukrat.net/124/deluge-webui-1-3-6-autologin-disable-password
# https://forum.deluge-torrent.org/viewtopic.php?f=7&t=54769&p=227493
RUN sed -i 's/if s.hexdigest() == config\["pwd_sha1"\]:/if True:/' /usr/lib/python2.7/dist-packages/deluge/ui/web/auth.py; \
    sed -i 's/onShow:function(){this.passwordField.focus(.*)}/onShow:function(){this.onLogin();}/' /usr/lib/python2.7/dist-packages/deluge/ui/web/js/deluge-all.js;
VOLUME /config
EXPOSE 8112/tcp
CMD ["deluge-web", "-c", "/config/"]
