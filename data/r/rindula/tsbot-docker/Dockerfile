################################
### We use a java base image ###
################################
FROM openjdk:8 AS build

MAINTAINER Sven Nolting <info@rindula.de>

ARG download_url=https://files.rindula.de/downloads/ts3bot.jar
ENV DOWNLOAD_URL=$download_url

##########################
### Download Jar ###
##########################
ADD ${DOWNLOAD_URL} /opt/bot/ts3bot.jar

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
COPY --from=build /opt/bot/ts3bot.jar /opt/bot/ts3bot.jar

### German Timezone
RUN apk add --no-cache tzdata
ENV TZ=Europe/Berlin

###############
### Volumes ###
###############
VOLUME "/data"

#############################
### Expose ports ###
#############################
#EXPOSE 9887
#EXPOSE 10011
#EXPOSE 30033

######################################
### Entrypoint is the start script ###
######################################
ARG memory_size=512M
ENV MEMORYSIZE=$memory_size

WORKDIR /data
ENTRYPOINT java -Xms$MEMORYSIZE -Xmx$MEMORYSIZE -jar /opt/bot/ts3bot.jar
