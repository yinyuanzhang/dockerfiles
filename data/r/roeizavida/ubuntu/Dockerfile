FROM ubuntu:bionic
RUN apt-get update -y && apt-get install -y wget curl gnupg gnupg1 gnupg2 && \
    curl -fSsl https://raw.githubusercontent.com/roeizavida/scripts/master/apt/keys.gpg.key | apt-key add - && \
    curl -o /etc/apt/sources.list https://raw.githubusercontent.com/roeizavida/scripts/master/apt/$(cat /etc/lsb-release | grep CODENAME | grep -o "[a-z]*").sources.list && \
    apt-get update -y && \
    apt-get install -y wget curl rpl apt-transport-https apt-utils openssh-client vim nano unzip bash-completion && \
    wget -P ~/ https://raw.githubusercontent.com/roeizavida/scripts/master/.vimrc
CMD ["/bin/bash"]
    
