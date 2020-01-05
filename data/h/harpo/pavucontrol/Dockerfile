FROM archlinux/base

LABEL maintainer "Harpo Roeder <roederharpo@protonmail.ch>"

RUN pacman -Syu --noconfirm && pacman -S --noconfirm pavucontrol

ENTRYPOINT ["pavucontrol"]
