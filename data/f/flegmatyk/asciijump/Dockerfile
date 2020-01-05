FROM ubuntu

MAINTAINER Michał Rudowicz <michal.rudowicz@fl9.eu>

RUN apt-get update && apt-get -y install asciijump

ENV TERM xterm-256color

CMD /bin/bash -c "sleep .1s && /usr/games/asciijump"

