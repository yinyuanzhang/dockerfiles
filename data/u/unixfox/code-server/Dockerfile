FROM codercom/code-server:v2

RUN curl -sL https://deb.nodesource.com/setup_13.x | sudo -E bash -

RUN sudo apt-get update && sudo apt-get install -y \
        openjdk-8-jdk \
        htop \
        liblz4-tool \
        nano \
        python3 \
        python3-pip \
        mysql-client \
        nodejs \
        libxss1 \
        libgtk-3-0 \
        liblombok-ast-java

WORKDIR /home/coder/project

VOLUME [ "/home/coder/project" ]

EXPOSE 8080

ENTRYPOINT ["dumb-init", "code-server", "--host", "0.0.0.0"]
