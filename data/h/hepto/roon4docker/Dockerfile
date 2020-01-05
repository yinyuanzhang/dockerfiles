FROM ubuntu 

WORKDIR /roon

RUN apt-get update && apt-get install -y \
	curl \	
	ffmpeg \
	cifs-utils

RUN curl http://download.roonlabs.com/builds/RoonServer_linuxx64.tar.bz2 | tar xvj

ENV ROON_DATAROOT=/roon/data

ENTRYPOINT ["/roon/RoonServer/start.sh"]



