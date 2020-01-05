FROM kunst1080/x11-base:latest
MAINTAINER kunst1080 kontrapunkt1080@gmail.com

RUN apt-get update \
        && DEBIAN_FRONTEND=noninteractive apt-get install -y \
            i3 \
            i3blocks \
            dmenu \
            j4-dmenu-desktop \
            lxterminal \
            feh \
            compton \
            parcellite \
            volumeicon-alsa \
            xsel \
            mirage \
            evince \
            lxrandr \
	&& rm -rf /var/lib/apt/lists/*

ADD xinitrc /xinitrc
RUN ln -s /xinitrc /root/.xinitrc
