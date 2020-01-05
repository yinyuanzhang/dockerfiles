FROM ubuntu:latest

# Replace the shell with bash for easier path sourcing
SHELL ["/bin/bash", "-c", "-l"]

RUN apt-get update
RUN apt-get install -y curl zip unzip git

RUN useradd --create-home --shell /bin/bash user

USER user
WORKDIR /home/user

RUN curl -s "https://get.sdkman.io" | bash

RUN echo '[ -s "$HOME/.sdkman/bin/sdkman-init.sh" ] && \. "$HOME/.sdkman/bin/sdkman-init.sh"  # This loads sdkman' | tee -a $HOME/.bashrc
RUN echo '[ -s "$HOME/.sdkman/bin/sdkman-init.sh" ] && \. "$HOME/.sdkman/bin/sdkman-init.sh"  # This loads sdkman' | tee -a $HOME/.profile


