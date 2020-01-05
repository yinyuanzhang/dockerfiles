FROM debian:jessie

# Installing packages
RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y binutils gcc libgtk2.0-0 libgtk2.0-dev psmisc vnc4server

ARG BASE_URL="http://downloads.sourceforge.net/project/lazarus/Lazarus%20Linux%20amd64%20DEB/Lazarus%20"

# Lazarus 1.8.2 https://sourceforge.net/projects/lazarus/files/Lazarus%20Linux%20amd64%20DEB/Lazarus%201.8.2/
ARG LAZ_VER="1.8.2"
ARG DEB_FPC="fpc_3.0.4-2_amd64.deb"
ARG DEB_FPC_SRC="fpc-src_3.0.4-2_amd64.deb"
ARG DEB_LAZARUS="lazarus-project_1.8.2-0_amd64.deb"

ADD ${BASE_URL}${LAZ_VER}"/"${DEB_FPC} .
ADD ${BASE_URL}${LAZ_VER}"/"${DEB_FPC_SRC} .
ADD ${BASE_URL}${LAZ_VER}"/"${DEB_LAZARUS} .

RUN dpkg -i ${DEB_FPC} && rm ${DEB_FPC}
RUN dpkg -i ${DEB_FPC_SRC} && rm ${DEB_FPC_SRC}
RUN dpkg -i ${DEB_LAZARUS} && rm ${DEB_LAZARUS}

# debugger
RUN apt-get install -y gdb

RUN apt-get clean && apt-get autoremove -y

# fcl-web http://wiki.lazarus.freepascal.org/fcl-web
RUN lazbuild --build-ide= --add-package /usr/share/lazarus/${LAZ_VER}/components/fpweb/weblaz.lpk

# for vnc4server
EXPOSE 5901
