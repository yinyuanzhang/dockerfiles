# Dockerfile for GOSSIP Masternodes
# https://gossipcoin.net/
# v0.1 - 2019-04-18

FROM phusion/baseimage
MAINTAINER Steven Mai <stevenmai@gossipcoin.net>
LABEL Name="dockerized GOSSIP masternode"
LABEL Publisher="official GOSSIP Project"

ARG USER_ID
ARG GROUP_ID

# set enviroment
ENV USER gossip
ENV HOME /${USER}
ENV USER_ID ${USER_ID:-1000}
ENV GROUP_ID ${GROUP_ID:-1000}

# set user and group
RUN groupadd -g ${GROUP_ID} ${USER} \
    && useradd -u ${USER_ID} -g ${USER} -s /bin/bash -m -d ${HOME} ${USER}

# download and unpack wallet
ADD https://bitbucket.org/GOSSIPCOIN/gossip/downloads/gossip-2.1.0-x86_64-linux.tar /tmp/
RUN tar -xvf /tmp/gossip-*.tar -C /tmp/
RUN cp /tmp/gossip-*/* /usr/local/bin
RUN rm -rf /tmp/gossip*

# set rights
RUN chmod a+x /usr/local/bin/*
RUN chown -R ${USER}:${USER} /${HOME}

EXPOSE 35501 46501

VOLUME ["${HOME}"]
WORKDIR ${HOME}
CMD ["gossipd"]
