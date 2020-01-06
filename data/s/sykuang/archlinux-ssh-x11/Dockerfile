FROM base/archlinux:latest
MAINTAINER sykuang <sykuang.tw@gmail.com>
ENV LANG=en_US.UTF-8

ARG USER=docker
ARG PASSWORD=docker
# Add Taiwan and US server to mirrolist
RUN curl https://www.archlinux.org/mirrorlist/?country=TW&country=US&protocol=http >> /etc/pacman.d/mirrorlist && \
    pacman -Syu --noconfirm && \
# Generate locale en_US
    sed -i 's/#en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/'  /etc/locale.gen && \
    echo "LANG=en_US.UTF-8" >> /etc/locale.conf && \
    locale-gen && \
# Install develop package
    pacman -S --noconfirm sudo git vim base-devel go && \
# Install yay
    useradd --create-home $USER && \
    echo -e "$USER\n$PASSWORD" | passwd $USER && \
    echo "$USER ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers && \
    cd /tmp && \
    sudo -u $USER git clone https://aur.archlinux.org/yay.git && \
    cd /tmp/yay && \
    sudo -u $USER makepkg -si --noconfirm && \
    cd / && \
    # Install HPN and X11
    runuser -l docker -c "yay --noconfirm -S openssh-hpn-git" && \
    pacman --noconfirm -S xterm xorg-xclock xorg-xcalc xorg-xauth xorg-xeyes ttf-droid && \
# Set SSH Server
    echo "Port 22" >> /etc/ssh/sshd_config && \
    echo "X11Forwarding yes" >> /etc/ssh/sshd_config && \
    echo "X11UseLocalhost no" >> /etc/ssh/sshd_config && \
    runuser -l $USER -c "touch ~/.Xauthority" && \
# Cleanup
    rm -rf /tmp/* && \
    rm -rf /usr/share/man/* && \
    rm -rf /usr/share/doc/* && \
    bash -c "echo 'y' | pacman -Scc >/dev/null 2>&1" && \
    rm -rf /var/lib/pacman/sync/*
# Add entrypoint.sh
ADD entrypoint.sh /etc/entrypoint.sh

EXPOSE 22
ENTRYPOINT ["/bin/bash","/etc/entrypoint.sh"]
