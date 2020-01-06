FROM debian:buster-slim
MAINTAINER daisukekobayashi <daisuke@daisukekobayashi.com>

ENV DEBIAN_FRONTEND noninteractive

ARG username=daisuke
ENV USER $username
ENV HOME /home/${USER}

RUN echo "deb http://deb.debian.org/debian buster non-free" \
      >> /etc/apt/sources.list.d/buster.non-free.list \
      && echo "deb http://security.debian.org/debian-security buster/updates non-free" \
      >> /etc/apt/sources.list.d/buster.non-free.list \
      && echo "deb http://deb.debian.org/debian buster-updates non-free" \
      >> /etc/apt/sources.list.d/buster.non-free.list

RUN apt-get update \
      && apt-get install -y locales \
      && localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias en_US.UTF-8 \
      && localedef -i ja_JP -c -f UTF-8 -A /usr/share/locale/locale.alias ja_JP.UTF-8 \
      && rm -rf /var/lib/apt/lists/*

ENV LANG en_US.utf8

RUN apt-get update \
      && apt-get install --no-install-recommends --no-install-suggests -y gnupg1 apt-transport-https ca-certificates

RUN apt-get update \
      && apt-get install --no-install-recommends --no-install-suggests -y xz-utils ca-certificates \
            zsh git curl wget vim-nox clang-format clang-tidy \
            make cmake build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev \
            llvm libncurses5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev \
            autoconf bison libyaml-dev libgdbm-dev ssh zip unzip rar unrar gawk \
            jq silversearcher-ag rsync cron w3m-img tree ctags connect-proxy tcptraceroute \
      && rm -rf /var/lib/apt/lists/*

RUN TEMP_DEB="$(mktemp)" \
      && curl -sL https://api.github.com/repos/BurntSushi/ripgrep/releases/latest \
          | jq -r '.assets[] | select(.browser_download_url | contains("deb")) | .browser_download_url' \
          | wget -O "$TEMP_DEB" -qi - \
      && dpkg -i "$TEMP_DEB" \
      && rm -f "$TEMP_DEB"

RUN apt-get update \
      && apt-get install --no-install-recommends --no-install-suggests -y \
            ninja-build gettext libtool libtool-bin autoconf automake cmake g++ pkg-config unzip \
      && rm -rf /var/lib/apt/lists/* \
      && git clone https://github.com/neovim/neovim \
      && cd neovim \
      && git checkout stable \
      && make CMAKE_BUILD_TYPE=Release && make install \
      && cd .. && rm -rf neovim

RUN apt-get update \
      && apt-get install --no-install-recommends --no-install-suggests -y automake xsel libevent-dev xdg-utils \
      && rm -rf /var/lib/apt/lists/* \
      && git clone https://github.com/tmux/tmux.git \
      && cd tmux \
      && git checkout $(git tag | sort -V | tail -n 1) \
      && sh autogen.sh \
      && ./configure \
      && make && make install \
      && cd .. && rm -rf tmux


RUN wget https://dl.google.com/go/go1.13.1.linux-amd64.tar.gz \
      && tar -C /usr/local -xzf go1.13.1.linux-amd64.tar.gz \
      && echo "PATH=$PATH:/usr/local/go/bin" \
          | tee -a /etc/profile \
      && rm go1.13.1.linux-amd64.tar.gz

RUN wget https://packages.erlang-solutions.com/erlang-solutions_1.0_all.deb \
      && dpkg -i erlang-solutions_1.0_all.deb \
      && apt-get update \
      && apt-get install --no-install-recommends --no-install-suggests -y esl-erlang elixir \
      && rm -rf /var/lib/apt/lists/*

RUN apt-get update \
      && apt-get install --no-install-recommends --no-install-suggests -y lsb-release \
      && export CLOUD_SDK_REPO="cloud-sdk-$(lsb_release -c -s)" \
      && echo "deb http://packages.cloud.google.com/apt $CLOUD_SDK_REPO main" \
          | tee -a /etc/apt/sources.list.d/google-cloud-sdk.list \
      && curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add - \
      && apt-get update -y && apt-get install google-cloud-sdk -y

SHELL ["/bin/zsh", "-c"]

RUN useradd --create-home --shell /bin/zsh ${USER}
USER ${USER}
WORKDIR /home/${USER}
