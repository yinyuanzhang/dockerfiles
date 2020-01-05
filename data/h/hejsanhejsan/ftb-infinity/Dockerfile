FROM java:8-jre

MAINTAINER Tummy

#This is the different ENV variables you will soon be able to modify some settings.
ENV motd Ljurs.se
ENV loginmotd Welcome!

ENV adminuuid 8aa6b4f2-81aa-4bf7-93de-4d8a453c9df4 \
	adminname Girltummy \
	backuptimer 1.0 \
	backupstokeep 12 \
	restarttimer 12.0



# Updating container
RUN apt-get update && \
	apt-get upgrade --yes --force-yes && \
	apt-get install -y nano && \
	apt-get clean && \ 
	rm -rf /var/lib/apt/lists/* 

# Setting workdir
WORKDIR /minecraft


# Changing user to root
USER root


# Creating user and downloading files
RUN useradd -m -U minecraft && \
	mkdir -p /minecraft/world && \
	wget -q http://addons-origin.cursecdn.com/files/2484/486/FTBInfinityServer_3.0.2.zip && \
	unzip -q FTBInfinityServer_3.0.2.zip && \
	rm FTBInfinityServer_3.0.2.zip && \
#Here is fixes permissions
	chmod u+x FTBInstall.sh ServerStart.sh && \
	echo "#By changing the setting below to TRUE you are indicating your agreement to our EULA (https://account.mojang.com/documents/minecraft_eula)." > eula.txt && \
	echo "$(date)" >> eula.txt && \
	echo "eula=TRUE" >> eula.txt && \
	chown -R minecraft:minecraft /minecraft
#This is stuff i added
RUN	wget -q https://raw.githubusercontent.com/akoj93/dockerfiles/master/ftb-infinity/3.0.2/server.properties && \
	wget -q https://raw.githubusercontent.com/akoj93/dockerfiles/master/ftb-infinity/3.0.2/config.json -P /minecraft/local/ftbu && \
	wget -q https://raw.githubusercontent.com/akoj93/dockerfiles/master/ftb-infinity/3.0.2/ops.json
RUN	sed -i "s/motd=.*/motd=${motd}/g" server.properties && \
	sed -i "s/    \"backup_timer\".*/    \"backup_timer\": $backuptimer,/g"  /minecraft/local/ftbu/config.json && \
	sed -i "s/    \"backups_to_keep\".*/    \"backups_to_keep\": $backupstokeep,/g"  /minecraft/local/ftbu/config.json && \
	sed -i "s/      \"Welcome to the server!\".*/      \"$loginmotd\"/g"  /minecraft/local/ftbu/config.json && \
	sed -i "s/    \"restart_timer\":.*/    \"restart_timer\": $restarttimer,/g"  /minecraft/local/ftbu/config.json && \
	sed -i "s/\[\].*/\[\n\{\n\"uuid\": \"$adminuuid\",\n\"name\": \"$adminname\",\n\"level\": 4\n\}\n\]/g" ops.json

	
	
# Running install
RUN /minecraft/FTBInstall.sh

# Expose port 25565
EXPOSE 25565

# Expose volumes
VOLUME /minecraft/world /minecraft/backups

# Start server
#You can only have one CMD. What is in cmd is what you get.
CMD ["/bin/bash", "/minecraft/ServerStart.sh"]
