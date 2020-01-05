FROM jonathonf/manjaro

MAINTAINER zalox

RUN mkdir -p /root/.gnupg /root/.gnupg/dirmngr-cache.d \
 && touch /root/.gnupg/dirmngr_ldapservers.conf \
 && pacman -Sy \
 && gpg -k \
 && pacman-key --init \
 && pacman-key --populate archlinux \
 && pacman-key --populate manjaro \
 && dirmngr < /dev/null \
 && pacman -S --noconfirm pacman-mirrors libusb ca-certificates \
 && pacman -Su --noconfirm \
 && pacman -Sc --noconfirm

