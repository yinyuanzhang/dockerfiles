FROM ubuntu:14.04

RUN apt-get update
RUN apt-get -y install vim tree curl wget git
RUN apt-get install -qqy x11-apps
RUN wget -qO- https://raw.githubusercontent.com/creationix/nvm/v0.33.11/install.sh | bash

WORKDIR spare

COPY * /spare/.devbox/

ENV TERM=xterm-256color

RUN echo "source /spare/.devbox/.bashprofile" >> /root/.bashrc

CMD ["/bin/bash"]