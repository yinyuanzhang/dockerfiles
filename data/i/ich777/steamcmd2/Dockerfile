FROM ich777/debian-baseimage

LABEL maintainer="admin@minenet.at"

RUN apt-get update && \
	apt-get -y install --no-install-recommends lib32gcc1 unzip && \
	rm -rf /var/lib/apt/lists/*

ENV DATA_DIR="/serverdata"
ENV STEAMCMD_DIR="${DATA_DIR}/steamcmd"
ENV SERVER_DIR="${DATA_DIR}/serverfiles"
ENV GAME_ID="template"
ENV GAME_NAME="template"
ENV GAME_PARAMS="template"
ENV GAME_PORT=27015
ENV VALIDATE=""
ENV ROCKET_MOD="true"
ENV ROCKET_URL="https://ci.rocketmod.net/job/Rocket.Unturned/lastSuccessfulBuild/artifact/Rocket.Unturned/bin/Release/Rocket.zip"
ENV ROCKET_FORCE_UPDATE=""
ENV UMASK=000
ENV UID=99
ENV GID=100
ENV USERNAME=""
ENV PASSWRD=""

RUN mkdir $DATA_DIR && \
	mkdir $STEAMCMD_DIR && \
	mkdir $SERVER_DIR && \
	useradd -d $DATA_DIR -s /bin/bash --uid $UID --gid $GID steam && \
	chown -R steam $DATA_DIR && \
	ulimit -n 2048

ADD /scripts/ /opt/scripts/
RUN chmod -R 770 /opt/scripts/ && \
	chown -R steam /opt/scripts

USER steam

#Server Start
ENTRYPOINT ["/opt/scripts/start-server.sh"]