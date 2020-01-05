FROM archlinux/base

LABEL maintainer "Harpo Roeder <roederharpo@protonmail.ch>"

RUN pacman -Syu --noconfirm && pacman -S --noconfirm noto-fonts-cjk noto-fonts-emoji noto-fonts-extra qtox

ENTRYPOINT ["qtox"]
