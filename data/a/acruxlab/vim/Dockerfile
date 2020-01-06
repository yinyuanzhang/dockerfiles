FROM debian:stretch-slim

ENV TERM screen-256color
ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update \
 && apt-get -y --no-install-recommends install curl exuberant-ctags git ca-certificates make cmake build-essential pkg-config libtool-bin m4 automake unzip libpthread-stubs0-dev gettext python3-dev python-dev python3-setuptools python-setuptools python3-pip python-pip flake8 ruby xclip xsel ruby-dev wget\ 
 && pip install wheel && pip install neovim\
 && pip3 install wheel && pip3 install neovim\
 && git clone https://github.com/neovim/libvterm.git && cd libvterm && make && make install && cd ../ && rm -rf libvterm \
 && git clone https://github.com/neovim/neovim.git nvim && cd nvim && make CMAKE_BUILD_TYPE=RelWithDebInfo && make install && cd .. && rm -rf nvim \
 && mkdir /root/.config && mkdir /root/.config/nvim && mkdir /root/.config/nvim/ftplugin && mkdir /root/.config/nvim/snippets && touch /root/.config/nvim/init.vim \
 && curl -fLo ~/.local/share/nvim/site/autoload/plug.vim --create-dirs https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim \
 && apt-get clean && rm -rf /var/lib/apt/lists/ \
 && gem install neovim \
 && curl -LO https://github.com/BurntSushi/ripgrep/releases/download/11.0.1/ripgrep_11.0.1_amd64.deb \
 && dpkg -i ripgrep_11.0.1_amd64.deb \
 && wget https://github.com/sharkdp/bat/releases/download/v0.11.0/bat_0.11.0_amd64.deb \
 && dpkg -i bat_0.11.0_amd64.deb

COPY init.vim /root/.config/nvim/init.vim
COPY ftplugin/ /root/.config/nvim/ftplugin/
COPY ultisnips/ /root/.config/nvim/ultisnips/
COPY NERDTreeBookmarks /root/.NERDTreeBookmarks
COPY flake8 /root/.config/flake8

RUN nvim "+set nomore" "+PlugInstall!" "+PlugClean" "+qall" \
 && ./root/.local/share/nvim/plugged/youcompleteme/install.py

ENTRYPOINT ["nvim"]
