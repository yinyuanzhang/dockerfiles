FROM cm2network/steamcmd:root

ENV SESSIONNAME="Ark Docker" \
	SERVERMAP=TheIsland \
	SERVERPASSWORD="" \
	ADMINPASSWORD="adminpassword" \
	SERVERPORT=27015 \
	STEAMPORT=7778 \
	BACKUPONSTART=0 \
	UPDATEONSTART=1 \
	BACKUPONSTOP=0 \
	WARNONSTOP=1 \
	NBPLAYERS=5 \
	RCONPORT=32330 \
	TERM=linux

# apt stuff is a separate layer
RUN apt-get update \
	&& apt-get dist-upgrade -y \
	&& apt-get install -y curl bzip2 libcompress-zlib-perl rsync \
	&& rm -rf /var/lib/apt/lists/*

# install arkmanager
RUN mkdir /ark \
	&& chown steam:steam /ark \
	&& curl -sL http://git.io/vtf5N | bash -s steam \
	&& ln -s /usr/local/bin/arkmanager /usr/bin/arkmanager \
	&& mkdir /home/steam/Steam \
	&& chown steam:steam /home/steam/Steam \
	&& mkdir /home/steam/ark-update \
	&& chown steam:steam /home/steam/ark-update

VOLUME  /ark 
ADD rootdir/ /

EXPOSE ${STEAMPORT}/udp ${SERVERPORT}/udp ${RCONPORT}/tcp

WORKDIR /ark
USER steam
ENTRYPOINT ["/home/steam/run.sh"]

