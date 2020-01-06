FROM ubuntu:19.04
RUN apt-get update && \
    apt install -y zsh amazon-ecr-credential-helper zip unzip curl docker && \
    curl -s "https://get.sdkman.io" | bash
SHELL ["/usr/bin/zsh", "-i", "-c"]
CMD ["/usr/bin/zsh", "-l", "-i"]