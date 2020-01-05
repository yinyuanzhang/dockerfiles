FROM debian:unstable

ENV DEBIAN_FRONTEND noninteractive

# Mises à jour et gestion de l'utf8
RUN echo deb http://httpredir.debian.org/debian stable main >> /etc/apt/sources.list; \
    echo deb http://httpredir.debian.org/debian experimental main >> /etc/apt/sources.list; \
    apt-get -y update ; apt-get -y dist-upgrade ; apt-get -y install gnupg2 ; apt-get -y autoremove --purge; \
    apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 742A4E8A1A1AB4339632CEB3E12CFAE2FE42299E; \
    echo deb http://ppa.launchpad.net/gregorio-project/gregorio/ubuntu xenial main >> /etc/apt/sources.list; \
    apt-get -y update; \
    apt-get -y install locales && \
    locale-gen C.UTF-8 && \
    /usr/sbin/update-locale LANG=C.UTF-8

ENV LC_ALL C.UTF-8


# Installation des programmes requis
RUN apt-get -y --force-yes install --no-install-recommends \
	texlive texlive-latex-recommended texlive-latex-extra texlive-xetex texlive-luatex \
	texlive-lang-european texlive-lang-french \
	texlive-humanities texlive-extra-utils \
	texlive-fonts-extra fonts-linuxlibertine lmodern texlive-metapost \
	texlive-music gregorio gregoriotex pandoc && \
    apt -y --force-yes install --no-install-recommends lilypond

ADD https://raw.githubusercontent.com/jperon/lyluatex/master/lyluatex-options.lua \
    https://raw.githubusercontent.com/jperon/lyluatex/master/lyluatex.lua \
    https://raw.githubusercontent.com/jperon/lyluatex/master/lyluatex-lib.lua \
    /usr/share/texlive/texmf-dist/scripts/lyluatex/

ADD https://raw.githubusercontent.com/jperon/lyluatex/master/lyluatex.sty \
    https://raw.githubusercontent.com/jperon/lyluatex/master/lyluatextools.sty \
    /usr/share/texlive/texmf-dist/tex/luatex/lyluatex/

RUN texhash
