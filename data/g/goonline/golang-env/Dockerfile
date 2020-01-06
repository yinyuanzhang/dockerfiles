FROM golang:1.12.7

RUN apt update && useradd -ms /bin/bash go-online && echo "root:root" | chpasswd && \
    apt-get install -y zsh wget git

ENTRYPOINT ["/main"]
USER go-online
RUN wget https://github.com/robbyrussell/oh-my-zsh/raw/master/tools/install.sh -O - | sh && \
    export TERM=xterm
USER root

ENV LANG=C.UTF-8
ENV TERM=xterm
