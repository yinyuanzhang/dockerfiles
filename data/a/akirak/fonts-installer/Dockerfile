FROM archlinux/base
RUN useradd -m arch
RUN echo "arch ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers
RUN pacman -Syy --noconfirm sudo git base-devel
RUN pacman -S --asdeps --noconfirm go
USER arch
WORKDIR /home/arch
RUN git clone https://aur.archlinux.org/yay.git
WORKDIR /home/arch/yay
RUN makepkg -si --noconfirm
WORKDIR /home/arch
RUN rm -rf /home/arch/yay
RUN sudo pacman -Rs --noconfirm go
RUN sudo pacman -Scc --noconfirm
RUN yay -S --noconfirm fontconfig freetype2 graphite libpng harfbuzz \
        xorg-bdftopcf libfontenc xorg-mkfontscale xorg-mkfontdir \
        xorg-font-util xorg-font-utils
ENTRYPOINT ["yay", "-S", "--noconfirm", "--noredownload"]
