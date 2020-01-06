# x11docker/lumina
# 
# Run lumina desktop in docker. 
# Use x11docker to run image. 
# Get x11docker from github: 
#   https://github.com/mviereck/x11docker 
#
# Run desktop with:
#   x11docker --desktop x11docker/lumina
#
# Run single application:
#   x11docker x11docker/lumina xterm
#
# Options:
# Persistent home folder stored on host with   --home
# Shared host folder with                      --sharedir DIR
# Hardware acceleration with option            --gpu
# Clipboard sharing with option                --clipboard
# Sound support with option                    --alsa
# With pulseaudio in image, sound support with --pulseaudio
# Printer support over CUPS with               --printer
# Webcam support with                          --webcam
#
# See x11docker --help for further options.

FROM voidlinux/voidlinux

RUN xbps-install -Suy lumina dbus liberation-fonts-ttf xterm \
         mesa-ati-dri mesa-intel-dri mesa-nouveau-dri kmod xz ||:

CMD start-lumina-desktop
