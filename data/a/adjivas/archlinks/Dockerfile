FROM base/archlinux
LABEL name="archlinks"
MAINTAINER adjivas <adjivas@student.42.fr>
RUN pacman -Syy
RUN pacman -S --noconfirm links
RUN mkdir $HOME/.links/
RUN touch $HOME/.links/links.his
ENV HOME /root
ENTRYPOINT ["links", "-anonymous", "https://www.duckduckgo.com"]
