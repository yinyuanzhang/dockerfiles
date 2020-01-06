FROM ubuntu:19.04
RUN mkdir /ep
env DEBIAN_FRONTEND=noninteractive HOME=/ep
RUN apt update \
    && apt install -y --no-install-recommends --allow-unauthenticated \
    xserver-xorg-core tigervnc-standalone-server tigervnc-xorg-extension \
    tigervnc-viewer ubuntu-gnome-desktop \
    && apt autoclean -y && apt autoremove -y && rm -rf /var/lib/apt/lists/* 
ADD xstartup /ep/.vnc/xstartup
ADD entrypoint.sh /ep/entrypoint.sh
ADD ep.sh /ep/ep.sh

RUN echo $(date "+%Y-%m-%d_%H:%M:%S" ) > /ep/btm \
    && chgrp -R 0 /ep  \
    && chmod -R g+rwx /ep 

ENTRYPOINT ["/ep/entrypoint.sh"]
USER 1001
