FROM ubuntu:latest
MAINTAINER Jonathan Carreño <jocarren@gmail.com>


#++++BEGIN SERVER COMMANDS AS ENVIRONMENT VARIABLES++++

#GENERAL
ENV HOSTNAME="Dockerized Cocaine Diesel Server"
ENV MAXCLIENTS="32"
ENV PUBLIC="1"

#++++END SERVER COMMANDS AS ENVIRONMENT VARIABLES++++


#++++BEGIN DIRECORY AND EXECUTABLE BUILD++++

ADD . /opt/cocaine
RUN useradd -m -s /bin/bash cocaine
RUN chown -R cocaine:cocaine /opt/cocaine
EXPOSE 44400/udp
EXPOSE 44400/tcp
WORKDIR /opt/cocaine
USER cocaine

#++++END DIRECORY AND EXECUTABLE BUILD++++

#++++BEGIN BINARY RUN++++

RUN chmod +x headlessupdater
RUN ./headlessupdater
CMD ./server +set fs_usehomedir "0" \
+set fs_basepath "/opt/cocaine/" \
+set sv_public "$PUBLIC" \
+set sv_hostname "$HOSTNAME" \
+set maxclients "$MAXCLIENTS"

#++++END BINARY RUN++++
