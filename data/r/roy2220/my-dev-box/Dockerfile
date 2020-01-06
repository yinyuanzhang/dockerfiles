FROM fedora:31

RUN dnf makecache \
    && dnf upgrade --assumeyes \
    && curl --silent --show-error --fail --request GET --location --output /etc/yum.repos.d/go-repo.repo \
            https://mirror.go-repo.io/fedora/go-repo.repo \
    && dnf makecache \
    && dnf remove --assumeyes \
           vi \
    && dnf autoremove --assumeyes \
    && dnf install --assumeyes \
           zsh tmux vim \
           git gcc gcc-c++ golang gdb make cmake ctags global the_silver_searcher cloc \
           stow gnupg proxychains-ng \
           findutils procps-ng xz \
           glibc-langpack-en redhat-rpm-config python-devel ncurses-compat-libs \
    && dnf clean all

RUN find "${HOME}" -mindepth 1 -name '*' -delete \
    && git clone --depth 1 --recurse-submodules https://github.com/roy2220/dotfiles.git "${HOME}/.files" \
    && stow --dir "${HOME}/.files" $(ls "${HOME}/.files")

RUN PATH=${PATH}:${HOME}/.local/bin \
    && get-direnv \
    && get-fzf \
    && LANG=en_US.UTF-8 LC_ALL=en_US.UTF-8 TERM=xterm-256color zsh -c 'source ~/.zplugrc && zplug install' < /dev/null \
    && echo | vim +PlugInstall +qall

ENV HOST=my-dev-box \
    LANG=en_US.UTF-8 \
    LC_ALL=en_US.UTF-8 \
    TZ=Asia/Shanghai

CMD ["/usr/bin/zsh", "--login"]
WORKDIR /root
