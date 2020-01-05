FROM debian:stretch-slim
LABEL maintainer "docker@danteimaginary.com"

## Information
# Build Image based on newest Debian strech Slim Image
# Installing Base features to download and running Steam unter debian stretch (Curl and Libs)
# Adding new User and Group (Steam) to run steam on restricted rights
# Adding Docker-Compose file, to outsource features like Content Adding and Server-Config
# After Steam installation, cleaning up Image to reduce discspace
# Expose only Port 27015 as UDP and TCP, there are no more ports needed for Playing Garry's Mod


# Base Installation
RUN addgroup steam && adduser --home /steam --disabled-password --ingroup steam steam \
 && apt-get update \
 && DEBIAN_FRONTEND=nointeractive \
 && apt-get -y upgrade \
 && apt-get -y install lib32gcc1 curl lib32stdc++6 lib32tinfo5 vim gdb net-tools \
 && su -l steam -c " \
 mkdir cmd && curl -sqL "https://steamcdn-a.akamaihd.net/client/installer/steamcmd_linux.tar.gz" | tar -C cmd -zxf - \
 && cmd/steamcmd.sh +login anonymous +quit \
 " \
 && apt-get -y remove curl \
 && apt-get -y autoremove \
 && apt-get -y clean \
 && apt-get -y purge


# Garrys Mod Installation
RUN DEBIAN_FRONTEND=nointeractive \
         && su -l steam -c "/steam/cmd/steamcmd.sh +login anonymous +force_install_dir /steam/gmod +app_update 4020 validate +quit"
# Creating Dirs
RUN DEBIAN_FRONTEND=nointeractive \
         && su -l steam -c "mkdir -p /steam/gmod/garrysmod/data && mkdir -p /steam/gmod/garrysmod/cache/srcds && mkdir -p /steam/gmod/garrysmod/cache/downloads && mkdir -p /steam/gmod/garrysmod/cache/downloadfiles"

USER steam
WORKDIR /steam/gmod
ENTRYPOINT ["./startscript"]

CMD ["run"]
