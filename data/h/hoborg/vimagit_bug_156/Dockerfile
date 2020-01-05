FROM ubuntu:14.04

ENV HOME=/root

# Install zsh etc.
RUN apt-get update && \
    apt-get install -y sudo zsh curl software-properties-common

# Add ppa's
RUN add-apt-repository -y ppa:neovim-ppa/unstable
RUN add-apt-repository -y ppa:git-core/ppa
RUN apt-get update

# Install neovim, git, vim-plug
RUN apt-get install -y neovim git
RUN curl -fLo ~/.config/nvim/autoload/plug.vim --create-dirs \
    https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim

# Configure git to prevent yapping about username
RUN git config --global user.email "an@example.com"
RUN git config --global user.name "Example Joe"

# Copy init.vim and install plugins
RUN mkdir -p $HOME/.config/nvim
ADD init.vim $HOME/.config/nvim/init.vim
RUN nvim +slient +VimEnter +PlugInstall +qall

CMD ["/usr/bin/zsh"]
