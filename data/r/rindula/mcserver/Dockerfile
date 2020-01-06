################################
### We use a java base image ###
################################
FROM openjdk:8 AS build

MAINTAINER Sven Nolting <info@rindula.de>

ARG paperspigot_ci_url=https://papermc.io/api/v1/paper/1.14.2/latest/download
ENV PAPERSPIGOT_CI_URL=$paperspigot_ci_url

##########################
### Download paperclip ###
##########################
ADD ${PAPERSPIGOT_CI_URL} /opt/minecraft/server/paperclip.jar

############################################
### Run paperclip and obtain patched jar ###
############################################
RUN cd /opt/minecraft/server/ \
    && java -jar paperclip.jar; exit 0

RUN cd /opt/minecraft/server/ \
    && mv cache/patched*.jar paperspigot.jar

###########################
### Running environment ###
###########################
FROM anapsix/alpine-java:8_server-jre_nashorn

#########################
### Working directory ###
#########################
WORKDIR /data

###########################################
### Obtain runable jar from build stage ###
###########################################
COPY --from=build /opt/minecraft/server/paperspigot.jar /opt/minecraft/server/paperspigot.jar

############################
### Obtain server config ###
###########################
ADD server.properties /opt/minecraft/server/server.properties
ADD server.properties /data/server.properties
ADD start.sh /data/start.sh

### German Timezone
RUN apk add --no-cache tzdata
ENV TZ=Europe/Berlin

###############
### Volumes ###
###############
VOLUME "/data"

###############	
### RCON   ###	
###############	
ARG RCON_CLI_VER=1.4.0	
ARG ARCH=amd64	
ADD https://github.com/itzg/rcon-cli/releases/download/${RCON_CLI_VER}/rcon-cli_${RCON_CLI_VER}_linux_${ARCH}.tar.gz /tmp/rcon-cli.tgz	
RUN tar -x -C /usr/local/bin -f /tmp/rcon-cli.tgz rcon-cli && \	
  rm /tmp/rcon-cli.tgz

#############################
### Expose minecraft port ###
#############################
EXPOSE 25565
# Queryport
EXPOSE 25566
# Dynmap?
EXPOSE 8123

######################################
### Entrypoint is the start script ###
######################################
ARG memory_size=3000M
ENV MEMORYSIZE=$memory_size

WORKDIR /data
ENTRYPOINT bash ./start.sh
