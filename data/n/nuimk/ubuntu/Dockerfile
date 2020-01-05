FROM ubuntu:16.04

RUN apt-get -y update \
    && apt-get -y upgrade \
    && apt-get -y install curl python3 tmux zsh \

    && locale-gen en_US.UTF-8 \
    && update-locale LANG=en_US.UTF-8 \

    # grab gosu for easy step-down from root
    && _GNUPG_HOME=$(mktemp -d) \
    && gpg --homedir=$_GNUPG_HOME --keyserver pool.sks-keyservers.net --recv-keys B42F6819007F00F88E364FD4036A9C25BF357DD4 \
    && curl -o /usr/local/bin/gosu -SL "https://github.com/tianon/gosu/releases/download/1.9/gosu-$(dpkg --print-architecture)" \
    && curl -o /usr/local/bin/gosu.asc -SL "https://github.com/tianon/gosu/releases/download/1.9/gosu-$(dpkg --print-architecture).asc" \
    && gpg --homedir=$_GNUPG_HOME --verify /usr/local/bin/gosu.asc /usr/local/bin/gosu \
    && rm /usr/local/bin/gosu.asc \
    && chmod +x /usr/local/bin/gosu \
    && rm -rf $_GNUPG_HOME \

    && rm -rf /var/lib/apt/lists/*
