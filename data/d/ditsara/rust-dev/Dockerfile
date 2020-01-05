FROM rust:latest
MAINTAINER Dan Itsara <dan@glazziq.com>

RUN apt update && \
  apt install -y neovim

RUN \
  # load bash-it and set aliases
  git clone --depth=1 https://github.com/Bash-it/bash-it.git ~/.bash_it && \
  ~/.bash_it/install.sh --silent --no-modify-config && \
  ln -s ~/.bash_it/aliases/available/vim.aliases.bash ~/.bash_it/enabled/150---vim.aliases.bash && \
  # install neovim plugin manager
  curl -fLo ~/.local/share/nvim/site/autoload/plug.vim --create-dirs \
    https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim

# build, install universal-ctags
RUN  git clone http://github.com/universal-ctags/ctags.git ~/ctags && \
  cd ~/ctags && \
  apt install -y autoconf make gcc automake && \
  ./autogen.sh && \
  ./configure --program-prefix=u && \
  make && make install && \
  # cleanup
  cd ~ && rm -rf ctags && \
  apt remove -y autoconf make gcc automake && apt autoremove -y

# build and install Racer (Rust auto-complete engine) into
# /usr/local/cargo/bin/racer
RUN rustup toolchain add nightly && \
  apt install -y build-essential cmake pkg-config zlib1g-dev libssl-dev && \
  cargo +nightly install racer && \
  apt remove -y build-essential cmake pkg-config zlib1g-dev libssl-dev

# add config files and install neovim plugins; separate layer so we don't need
# to re-build everything when we change plugins or add files to home directory
ADD dev/home /root
RUN nvim -E -u NONE -S ~/.config/nvim/init.vim +PlugInstall +qall > /dev/null || true

WORKDIR /app
ENV DISPLAY=:0
