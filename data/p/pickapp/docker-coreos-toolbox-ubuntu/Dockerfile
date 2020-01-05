FROM ubuntu:latest
MAINTAINER Adam Wallner <wallner@bitbaro.hu>

RUN \
    # Upgrade
    apt-get update && apt-get upgrade -y && \
    # Add needed users and groups
    addgroup --gid 500 core && \
    adduser --home /home/core --shell /bin/bash --uid 500 --gid 500 --disabled-password --system core && \
    addgroup --gid 253 fleet && \
    adduser core fleet && \
    addgroup --gid 233 coredocker && \
    adduser core coredocker && \
    addgroup --gid 248 core-systemd-journal && \
    adduser core core-systemd-journal && \
    # Install needed packages
    apt-get install -y sudo net-tools inetutils-ping bash-completion mc tmux openssh-client && \
    apt-get clean && \
    # This is needed by host docker
    ln -s /lib/x86_64-linux-gnu/libdevmapper.so.1.02.1 /lib/x86_64-linux-gnu/libdevmapper.so.1.02 && \
    # Sudo without password
    sed -i "s/%sudo\s*ALL=(ALL:ALL)\s*ALL/%sudo ALL=(ALL:ALL) NOPASSWD:ALL/" /etc/sudoers && \
    # Add core user to sudoers
    adduser core sudo && \
    # Bypass original bashrc
    mv /etc/bash.bashrc /etc/bash.basrc.coreos && \
    echo ". /etc/bash.bashrc.coreos\nPS1=\"\\[\\033[01;35m\\]toolbox\\[\\033[01;34m\\] \$PS1\"" >/etc/bash.bashrc
    
WORKDIR /home/core

ENTRYPOINT ["/bin/bash"]
