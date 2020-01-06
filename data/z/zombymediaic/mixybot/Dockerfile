FROM ubuntu

MAINTAINER zombymediaic

# Update aptitude with new repo
#lol
RUN apt update
RUN apt-get update && apt-get install -y --no-install-recommends apt-utils

RUN apt-get update && apt-get install -y wget nano git curl vim htop gnupg2 openjdk-8-jdk
RUN apt update

WORKDIR shisha_bot/

RUN wget http://cdn.zombymedia.com/discord/music-bot/musicBot.jar
RUN wget http://cdn.zombymedia.com/discord/music-bot/config.txt
RUN wget http://cdn.zombymedia.com/discord/music-bot/default.txt && mkdir Playlists && mv default.txt Playlists/default.txt
RUN echo "{\n}" >> serversettings.json

EXPOSE 3000
