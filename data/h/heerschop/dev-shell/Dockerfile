FROM ubuntu:17.04

MAINTAINER Heerschop

ENV NVM_DIR "$HOME/.nvm"
ENV TERM xterm
ENV SHELL /bin/zsh

RUN apt-get update \
 && apt-get install --yes --no-install-recommends \
    ca-certificates \
    git    \
    curl   \
    python \
    less   \
    sudo   \
    zsh

RUN sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)" || :
RUN curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.33.2/install.sh | zsh
RUN . "$NVM_DIR/nvm.sh" && nvm install node

CMD ["/bin/zsh"]
