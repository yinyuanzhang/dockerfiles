FROM thomaskatalis/rpi-raspbian:stretch

RUN [ "cross-build-start" ]

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update

RUN apt-get install -y chromium-browser
RUN apt-get install -y xserver-xorg-core
RUN apt-get install -y xserver-xorg-video-fbdev
RUN apt-get install -y x11-xserver-utils
RUN apt-get install -y libgl1-mesa-dri
RUN apt-get install -y matchbox-window-manager
RUN apt-get install -y xautomation
RUN apt-get install -y feh
RUN apt-get install -y xauth
RUN apt-get install -y libraspberrypi0 libraspberrypi-dev libraspberrypi-doc libraspberrypi-bin
RUN apt-get install -y xinit

ADD run /bin/run
ADD wallpaper.png /etc/wallpaper.png

RUN adduser --system --uid 5000 --disabled-password --shell /bin/bash  -q chromium
RUN addgroup chromium tty

RUN [ "cross-build-end" ]

ADD start-chromium /root/start-chromium

ENV XINITRC=/root/start-chromium
ENTRYPOINT [ "/bin/run" ]
