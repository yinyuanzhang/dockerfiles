FROM archlinux/base
# installing yay
RUN pacman -Syu --noconfirm && \
    pacman -S --noconfirm git binutils sudo go make gcc fakeroot gawk file && \
    git clone https://aur.archlinux.org/yay.git && \
    useradd builder -m && \
    passwd -d builder && \
    printf 'builder ALL=(ALL) ALL\n' | tee -a /etc/sudoers && \
    chmod 777 /yay && \
    su - builder -c "cd /yay && makepkg -s" && \
    pacman -U --noconfirm /yay/yay-*.pkg.tar* && \
    pacman -R --noconfirm go make gcc gawk && \
    rm -rf /var/cache /yay

ADD yay /usr/local/bin
