FROM ubuntu:17.10

ONBUILD CMD ["/bin/zsh"]

WORKDIR /root

RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y \
    build-essential \
    language-pack-ja  \
    zsh \
    git \
    emacs \
&& apt-get clean \
&& rm -rf /var/lib/apt/lists/*

RUN ln -sf /usr/share/zoneinfo/Asia/Tokyo /etc/localtime

RUN echo 'export LANG=ja_JP.UTF-8' >> .zshrc \
 && echo 'export LC_ALL=ja_JP.UTF-8' >> .zshrc

RUN if [ ! -d .ssh ]; then mkdir .ssh; fi \
 && chmod 700 .ssh \
 && ssh-keyscan -H github.com >> .ssh/knownhosts

RUN git clone https://github.com/nukosuke/dotfiles ~/dotfiles \
 && mv ~/dotfiles/.emacs.d ~/

ENTRYPOINT ["emacs"]
