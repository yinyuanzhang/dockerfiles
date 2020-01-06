FROM patricol/arch

RUN sort-mirrors \
 && addpackages \
    git keychain openssh curl wget man \
    neofetch powerline powerline-vim htop bash-completion ranger tmux zsh fortune-mod cowsay \
    pkgfile \
 && sudo ln -s /usr/local/bin /scripts \
 && sudo touch /scripts/setup /scripts/update /scripts/dotfiles /scripts/start /scripts/clearcache \
 && sudo chown user:users /scripts/* \
 && chmod +x /scripts/* \
 && echo "sort-mirrors; addpackages" >> /scripts/update \
 && git clone -b dockerarch --bare https://github.com/Patricol/dotfiles.git ~/.dotfiles-repo \
 && git --git-dir=$HOME/.dotfiles-repo/ --work-tree=$HOME config --local status.showUntrackedFiles no \
 && git --git-dir=$HOME/.dotfiles-repo/ --work-tree=$HOME checkout -f \
 && echo "git --git-dir=\$HOME/.dotfiles-repo/ --work-tree=\$HOME fetch origin dockerarch" >> /scripts/dotfiles \
 && echo "git --git-dir=\$HOME/.dotfiles-repo/ --work-tree=\$HOME reset --hard FETCH_HEAD" >> /scripts/dotfiles \
 && echo "dotfiles" >> /scripts/setup \
 && echo "type ~/refresh && source ~/refresh" >> /scripts/setup \
 && echo "echo 'skipping update'" >> /scripts/setup \
 && echo "start" >> /scripts/setup \
 && echo "exec bash" > /scripts/start \
 && echo "yay --noconfirm -c" >> /scripts/clearcache \
 && echo "(yes | yay -Scc || true)" >> /scripts/clearcache \
 && clearcache

CMD /bin/bash -c /scripts/setup
