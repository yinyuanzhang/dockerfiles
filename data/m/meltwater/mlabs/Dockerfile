FROM debian:stretch

USER root
RUN apt-get update && apt-get install -y \
    awscli \
    colordiff \
    curl \
    dnsutils \
    gawk \
    git \
    httpie \
    jq \
    locales \
    lua-nvim \
    mariadb-client \
    mongo-tools \
    neovim \
    net-tools \
    nmap \
    p7zip \
    python \
    python-pip \
    redis-tools \
    rsync \
    ruby-neovim \
    silversearcher-ag \
    traceroute \
    vim \
    wget \
    zplug \
    zsh \
    apt-transport-https \
    gnupg \
 && wget -qO- https://packages.microsoft.com/keys/microsoft.asc | apt-key add - \
 && echo "deb [arch=amd64] https://packages.microsoft.com/debian/9/prod stretch main" \
    | tee /etc/apt/sources.list.d/mssql-cli.list \
 && apt-get update && apt-get install -y \
    mssql-cli \
 && rm -rf /var/lib/apt/lists/*

RUN pip install \
    awscurl

RUN localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias en_US.UTF-8
ENV LANG en_US.utf8

COPY zshrc /root/.zshrc
RUN chsh -s /bin/zsh root

WORKDIR /root

ENTRYPOINT ["zsh"]
