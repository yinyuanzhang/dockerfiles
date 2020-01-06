FROM 		debian:stable-slim 
MAINTAINER	jeroen@pyromanic.nl
RUN		apt-get update &&\
		apt-get dist-upgrade -y &&\
		apt-get clean
ADD 		https://github.com/just-containers/s6-overlay/releases/download/v1.21.8.0/s6-overlay-amd64.tar.gz /tmp/
RUN 		tar xzvf /tmp/s6-overlay-amd64.tar.gz -C / &&\
	 rm /tmp/s6-overlay-amd64.tar.gz
ENTRYPOINT 	["/init"]
CMD 		["/bin/bash"]
