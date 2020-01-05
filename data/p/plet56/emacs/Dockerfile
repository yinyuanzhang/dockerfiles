FROM silex/emacs:26.3

RUN apt-get update
RUN apt-get -y install git

RUN useradd -G sudo -u 1000 --create-home emacs

ADD --chown=emacs init-emacs.el /home/emacs/init-emacs.el
RUN su emacs -c "emacs --script /home/emacs/init-emacs.el"

ADD --chown=emacs dotemacs /home/emacs/.emacs

ENV HOME /home/emacs
WORKDIR /home/emacs

