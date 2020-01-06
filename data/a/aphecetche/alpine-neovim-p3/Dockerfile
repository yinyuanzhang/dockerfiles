FROM aphecetche/alpine-neovim-base:latest

RUN apk add --update-cache --no-cache git python3 && \ 
    apk add --no-cache --virtual build-deps musl-dev gcc python3-dev && \
    python3 -m ensurepip && \
    pip3 install --upgrade pip setuptools && \
    pip3 install neovim && \
    git clone --depth=1 https://github.com/aphecetche/dotfiles.git && \
    mkdir /root/.config && \
    mv dotfiles/config/nvim /root/.config/ && \
    ln -s /root/.config/nvim /root/.vim && \
    ln -s /root/.config/nvim/init.vim /root/.vimrc && \
    nvim --headless -c "PlugInstall! | qall! " && \
    nvim --headless +UpdateRemotePlugins +qall && \
    apk del build-deps


ENV BACKGROUND=light
ENV THEME=base16-solarized

