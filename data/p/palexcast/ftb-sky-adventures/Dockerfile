FROM java:8-jre

MAINTAINER Patricio Alexander Castillo (https://github.com/palexcast)

# Setup args
ARG URI=https://www.feed-the-beast.com/projects/ftb-sky-adventures/files/2638383/download

# Updating container
RUN apt-get update && \
	apt-get upgrade --yes --force-yes && \
	apt-get clean && \
	rm -rf /var/lib/apt/lists/*

# Setting workdir
WORKDIR /minecraft

# Changing user to root
USER root

# Creating user and downloading files
RUN useradd -m -U minecraft && \
	mkdir -p /minecraft/world && \
	wget -O server.zip $URI && \
	unzip server.zip && \
	rm server.zip && \
	chmod u+x FTBInstall.sh ServerStart.sh && \
	echo "#By changing the setting below to TRUE you are indicating your agreement to our EULA (https://account.mojang.com/documents/minecraft_eula)." > eula.txt && \
	echo "$(date)" >> eula.txt && \
	echo "eula=TRUE" >> eula.txt && \
	chown -R minecraft:minecraft /minecraft

# Changing user to minecraft
USER minecraft

# Running install
RUN /minecraft/FTBInstall.sh

COPY settings-local.sh /minecraft/settings-local.sh

# Expose port 25565
EXPOSE 25565
EXPOSE 25565/udp

# Expose volume
VOLUME ["/minecraft/world"]

# Start server
CMD ["/bin/bash", "/minecraft/ServerStart.sh"]