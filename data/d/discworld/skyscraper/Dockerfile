FROM archlinux/base:latest

RUN pacman -Syu --noconfirm

RUN pacman -S qt5-base base-devel wget p7zip --noconfirm

ENV HOME /root
WORKDIR ${HOME}

ADD build-skyscraper.sh ${HOME}
RUN chmod +x ${HOME}/build-skyscraper.sh && ./build-skyscraper.sh

ADD bash_profile ${HOME}/.bash_profile

RUN rm ${HOME}/build-skyscraper.sh
RUN pacman -Scc --noconfirm

VOLUME /roms
VOLUME /config

RUN ln -s /config $HOME/.skyscraper

ENV LANG en_US.UTF-8

CMD ["/usr/bin/bash"]
