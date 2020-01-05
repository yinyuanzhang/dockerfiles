
FROM mono:latest

LABEL maintainer="frostbytes"

ARG SMOD_VERSION=3.5.0
ARG MULTIADMIN_VERSION=3.2.1

ENV SCPSL_APPID=996560 \
    SCPSL_INSTALLDIR=/opt/scpsl \
    SCPSL_CONFIGDIR=${SCPSL_INSTALLDIR}/config \
    SCPSL_PLUGINDIR=${SCPSL_INSTALLDIR}/sm_plugins \
    SCPSL_DATADIR=/home/scpsl/.config/SCP\ Secret\ Laboratory \
    SCPSL_LOGDIR=${SCPSL_INSTALLDIR}/logs \
    SMOD_URL=https://github.com/Grover-c13/Smod2/releases/download/${SMOD_VERSION} \
    MULTIADMIN_URL=https://github.com/Grover-c13/MultiAdmin/releases/download/${MULTIADMIN_VERSION} \
    STEAMCMD_INSTALLDIR=/opt/steamcmd

# set -x
RUN set -x

# first, get dependencies and clean
RUN apt-get update && \
    apt-get install -y --no-install-recommends --no-install-suggests lib32stdc++6 lib32gcc1 wget ca-certificates && \
    apt-get clean autoclean && \
    apt-get autoremove -y && \
    rm -rf /var/lib/{apt,dpkg,cache,log}/

# get steamcmd and place it in directory
RUN mkdir -p ${STEAMCMD_INSTALLDIR} && \
    cd ${STEAMCMD_INSTALLDIR} && \
    wget -qO- 'https://steamcdn-a.akamaihd.net/client/installer/steamcmd_linux.tar.gz' | tar zxf -

# install SCP Server
RUN ${STEAMCMD_INSTALLDIR}/steamcmd.sh \
      +login anonymous \
      +force_install_dir ${SCPSL_INSTALLDIR} \
      +app_update ${SCPSL_APPID} -beta linux validate \
      +quit

# install SMod2
RUN wget -qO- ${SMOD_URL}/Smod2.dll > ${SCPSL_INSTALLDIR}/SCPSL_Data/Managed/Smod2.dll && \
    wget -qO- ${SMOD_URL}/Assembly-CSharp.dll > ${SCPSL_INSTALLDIR}/SCPSL_Data/Managed/Assembly-CSharp.dll

# install MultiAdmin
RUN wget -qO- ${MULTIADMIN_URL}/MultiAdmin.exe > ${SCPSL_INSTALLDIR}/MultiAdmin.exe

# install multiadmin config
ADD scp_multiadmin.cfg ${SCPSL_INSTALLDIR}/scp_multiadmin.cfg

# make directories
RUN mkdir -p ${SCPSL_CONFIGDIR} && \
    mkdir -p ${SCPSL_PLUGINDIR}

# initialize users and permissions
RUN useradd -m scpsl && \
    chown -R scpsl:scpsl ${SCPSL_INSTALLDIR}

# fix runtime values
USER scpsl

WORKDIR ${SCPSL_INSTALLDIR}

VOLUME ${SCPSL_CONFIGDIR}
VOLUME ${SCPSL_PLUGINDIR}
VOLUME ${SCPSL_INSTALLDIR}
VOLUME ${SCPSL_LOGDIR}

EXPOSE 7777/tcp
EXPOSE 7777/udp

ENTRYPOINT mono ${SCPSL_INSTALLDIR}/MultiAdmin.exe
