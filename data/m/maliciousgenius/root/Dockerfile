FROM ubuntu

# apt conf
ENV DEBIAN_FRONTEND=noninteractive

# apt update & upgrade
RUN apt-get update --quiet ; \
    apt-get upgrade --quiet --yes ;

# configure deb-backend
RUN echo "debconf debconf/frontend select noninteractive" | debconf-set-selections ; \
    dpkg-reconfigure --frontend=noninteractive debconf ; \
    # do not exclude man pages & other documentation
    rm /etc/dpkg/dpkg.cfg.d/excludes ;

# install some the packages to full system provision
RUN apt-get install --quiet --yes --no-install-recommends \
        ca-certificates \
        apt-transport-https \
        software-properties-common \
        apt-utils \
        gnupg ;

# common pakages
RUN apt-get install --quiet --yes --no-install-recommends \
        # ru lang support
        locales language-pack-ru-base \
        # time data
        tzdata ;

# clearnup apt
RUN apt-get autoremove --yes ; \
    apt-get clean ; \
    rm -rf /var/lib/apt/lists/* ;

# подпись
LABEL MAINTAINER="Dmitriy Detkov"
LABEL MAIL="maliciousgenius@gmail.com"
LABEL TEL="+79604565686"
