FROM ubuntu:18.04

RUN apt-get update && apt-get upgrade -y && apt-get install -y openjdk-8-jre wget && mkdir /minecraft

ARG STARTUP_SCRIPT=/minecraft/ServerStart.sh

VOLUME /minecraft
EXPOSE 25565
EXPOSE 9010

CMD chown -R root /minecraft && touch $STARTUP_SCRIPT && chmod +x $STARTUP_SCRIPT
ENTRYPOINT $STARTUP_SCRIPT
