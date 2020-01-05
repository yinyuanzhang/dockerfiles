FROM ubuntu:19.04
LABEL maintainer "Sleepy Mario <theonesleepymario@gmail.com>"

RUN echo 'deb [arch=amd64,i386 trusted=yes] http://repo.steampowered.com/steam precise steam' > /etc/apt/sources.list.d/steam-inst.list && dpkg --add-architecture i386

RUN apt-get update \
	&& apt-get upgrade -yq
RUN apt-get install -yq --no-install-recommends sudo steam-launcher ca-certificates \
	&& rm -rf /etc/apt/sources.list.d/steam-inst.list 
RUN echo 'deb [trusted=yes] http://ppa.launchpad.net/oibaf/graphics-drivers/ubuntu disco main' > /etc/apt/sources.list.d/graphics.list
RUN echo 'deb-src [trusted=yes] http://ppa.launchpad.net/oibaf/graphics-drivers/ubuntu disco main ' >> /etc/apt/sources.list.d/graphics.list
RUN apt-get update 
RUN apt-get upgrade -yq 

RUN DEBIAN_FRONTEND=noninteractive apt-get install -yq xdg-utils \
	libgl1-mesa-dri libgl1-mesa-dri:i386 libgl1-mesa-glx:i386 libc6:i386 libnss3:i386 dbus:i386 dbus-x11:i386 mesa-vdpau-drivers mesa-vdpau-drivers:i386 libxss1 libxss1:i386 xorg pkg-config binutils pciutils pulseaudio libcanberra-gtk-module \
        libopenal1 libnss3 libgconf-2-4 libxss1 libnm-glib4 \
        libnm-util2 libglu1-mesa locales libsdl2-image-2.0 \
        mesa-utils:i386 \
        libstdc++5 libstdc++5:i386 libbz2-1.0:i386 \
        libsdl2-2.0-0 libsdl2-2.0-0:i386 \
        libgl1-mesa-dri:i386 libgl1-mesa-glx:i386 libc6:i386 \
        libxtst6:i386 libxrandr2:i386 libglib2.0-0:i386 \
        libgtk2.0-0:i386 libgdk-pixbuf2.0-0:i386 libsm6:i386 \
        libice6:i386 libopenal1:i386 libdbus-glib-1-2:i386 \
        libnm-glib4:i386 libnm-util2:i386 libusb-1.0-0:i386 \
        libnss3:i386 libgconf-2-4:i386 libxss1:i386 libcurl4:i386 \
        libv8-dev:i386 \
        libcanberra-gtk-module:i386 libpulse0:i386 attr libxtst6 libxtst6:i386 \
	mesa-vulkan-drivers mesa-vulkan-drivers:i386 -y \
	fonts-liberation fonts-wqy-zenhei

RUN apt-get autoremove -y && \
	apt-get autoclean -y &&\
	apt-get clean -y

RUN echo 'en_US.UTF-8 UTF-8' > /etc/locale.gen
RUN locale-gen
RUN echo 'en_US.UTF-8' > /etc/locale.conf

RUN echo 'steam ALL = NOPASSWD: ALL' > /etc/sudoers.d/steam
RUN chmod 0440 /etc/sudoers.d/steam
RUN adduser --disabled-password steam --gecos "Steam"

USER steam
ENV HOME /home/steam
ENV PULSE_SERVER unix:/tmp/pulse

CMD sudo /etc/init.d/dbus start && steam
