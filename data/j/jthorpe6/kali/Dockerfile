# From base kali
FROM kalilinux/kali-linux-docker

# Set working dir
WORKDIR /root/

ENV LC_ALL C.UTF-8

# kali installs
RUN apt-get update && apt-get upgrade -y && apt-get install -y \
    emacs \
    zsh \
    git \
    python-pip \
    tmux \
    apt-get -y autoremove && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN pip install \
    pipenv

# GitHub stuff

# ZSH
RUN git clone --recursive https://github.com/sorin-ionescu/prezto.git "${ZDOTDIR:-$HOME}/.zprezto" && \
    ln -s ~/.zprezto/runcoms/zlogin ~/.zlogin && \
    ln -s ~/.zprezto/runcoms/zlogout ~/.zlogout && \
    ln -s ~/.zprezto/runcoms/zpreztorc ~/.zpreztorc && \
    ln -s ~/.zprezto/runcoms/zprofile ~/.zprofile && \
    ln -s ~/.zprezto/runcoms/zshenv ~/.zshenv && \
    ln -s ~/.zprezto/runcoms/zshrc ~/.zshrc && \
    echo "export TERM=screen-256color" >> ~/.zshrc && \
    echo "unset TMPDIR" >> ~/.zshrc && \
    echo "alias em=emacs" >> ~/.zshrc && \
    echo "alias rm=rm" >> ~/.zshrc
    
# set ZSH shell as entry point
ENTRYPOINT ["/bin/zsh"]
