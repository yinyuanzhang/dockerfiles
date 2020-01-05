FROM debian as jdk-debian

RUN apt update && \
    apt upgrade -y && \
    apt install -y openjdk-8-jdk curl bash zip git make gnupg2 apt-transport-https software-properties-common && \
    curl -fsSL https://download.docker.com/linux/debian/gpg | apt-key add - && \
    add-apt-repository \
       "deb [arch=amd64] https://download.docker.com/linux/debian \
       $(lsb_release -cs) \
       stable" && \
    apt update && \
    apt install -y docker-ce && \
    bash -c 'curl -s "https://get.sdkman.io" | bash'

FROM jdk-debian

RUN bash -c 'source "$HOME/.sdkman/bin/sdkman-init.sh"; sdk install sbt 1.1.6' && \
    ln -s $HOME/.sdkman/candidates/sbt/current/bin/sbt /usr/local/bin/sbt && \
    curl -L https://git.io/n-install | bash -s -- -y && \
    ln -s /root/n/bin/n /usr/local/bin/n
