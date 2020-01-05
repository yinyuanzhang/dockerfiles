FROM patricol/gui_base_initial:arch

ENV RESOLUTION="1920x1080"
ENV PASSWORD="Password"
#8 char max if using VNC.
ENV RDP_OR_VNC="RDP"

RUN sudo touch /scripts/vnc_start /scripts/rdp_start /scripts/startapp \
 && sudo chown user:users /scripts/* \
 && chmod +x /scripts/* \
 && sort-mirrors \
#setup VNC
 && addpackages tigervnc \
 && mkdir -p ~/.vnc \
 && touch ~/.vnc/passwd \
 && echo '#!/bin/bash' >> ~/.vnc/xstartup \
 && echo 'exec i3' >> ~/.vnc/xstartup \
 && chmod -R go-rwx ~/.vnc \
 && chmod 755 ~/.vnc/xstartup \
 && echo "echo \"\$PASSWORD\" | vncpasswd -f >> ~/.vnc/passwd" >> /scripts/vnc_start \
 && echo "sudo rm -f /tmp/.X0-lock /tmp/.X11-unix/X0" >> /scripts/vnc_start \
 && echo "vncserver :0 -fg -geometry \$RESOLUTION" >> /scripts/vnc_start \
#xrdp depends on tigervnc; and installing tigervnc first prevents aurman from asking which way to resolve dependencies when installing xrdp.
#setup RDP
 && addpackages xrdp \
 && echo "i3" > ~/.xsession \
 && echo 'export QT_XKB_CONFIG_ROOT=/usr/share/X11/locale' | sudo tee -a /etc/profile \
 && echo 'echo "user:$PASSWORD" | sudo chpasswd' >> /scripts/rdp_start \
 && echo "sudo xrdp-sesman" >> /scripts/rdp_start \
 && echo "sudo xrdp --nodaemon" >> /scripts/rdp_start \
#wrap up
 && echo 'case "$RDP_OR_VNC" in "RDP") rdp_start;; "VNC") vnc_start;; "DEBUG") bash;; *) rdp_start;; esac' > /scripts/start \
 && clearcache

EXPOSE 3389
EXPOSE 5900
