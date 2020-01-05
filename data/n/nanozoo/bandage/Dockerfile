FROM ubuntu:bionic
ENV VERSION 0.8.1
ENV VERSIONGIT v0_8_1 
# replace the dots with _ in versiongit

RUN apt-get update
RUN	apt-get install --no-install-recommends -y \
		unzip \
		wget \
		libx11-xcb1 \
		libxcb-glx0 \
		libfontconfig1 \
		libgl1 \
		ncbi-blast+ \
		libx11-6 \
		procps \
		software-properties-common


RUN wget --no-check-certificate https://github.com/rrwick/Bandage/releases/download/v$VERSION/Bandage_Ubuntu_static_$VERSIONGIT.zip

RUN 	unzip Bandage_Ubuntu_static_$VERSIONGIT.zip && mv Bandage /usr/local/bin/ 
	
RUN 	apt-get clean all && \
	apt-get autoremove -y --purge unzip && \
	rm Bandage_Ubuntu_static_$VERSIONGIT.zip && \
	apt-get purge && \
	rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*



