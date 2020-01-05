FROM archlinux/base

LABEL maintainer "Harpo Roeder <roederharpo@protonmail.ch>"

RUN pacman -Syu --noconfirm && pacman -S --noconfirm dbus noto-fonts gpodder

ENTRYPOINT ["gpodder"]
