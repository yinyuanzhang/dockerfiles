# Dockerfile
FROM  debian:buster-slim

LABEL maintainer="RogueThorn"
LABEL support="https://livesupport.ts3musicbot.net"
LABEL description="[Offical] TS3MusicBot.net Docker Image - One Image - endless Bots"

USER root
COPY root/ /

ENV LC_ALL="C"
ARG DATE_ARG 
ARG SOURCE_BRANCH_ARG 
ARG SOURCE_COMMIT_ARG 
ARG DOCKER_REPO_ARG 
ARG CACHE_TAG_ARG 
ARG IMAGE_NAME_ARG 
ARG MICROSCAN_ARG 

RUN DEBIAN_FRONTEND=noninteractive
RUN apt -y update && \
	apt -y upgrade && \
	apt -y dist-upgrade && \
	mkdir /usr/share/man/man1 && \
	apt install -y --no-install-recommends ca-certificates apt-utils psmisc procps xauth bzip2 libmp3lame-dev libssl-dev curl unzip wget mplayer xvfb libglib2.0-0 libxrender-dev libxrandr2 libxcursor-dev libx11-xcb-dev python libavcodec-extra58 libavcodec-extra xdotool x11-utils libgl1-mesa-dri x11-xkb-utils libegl1-mesa libpci3 libxslt1.1 screen nano libdbus-glib-1-2 && \ 
	apt install -y default-jre && \
	apt install -y --reinstall xkb-data
RUN wget http://ftp.us.debian.org/debian/pool/main/libt/libtasn1-6/libtasn1-6_4.14-3_amd64.deb && \
	dpkg -i libtasn1-6_4.14-3_amd64.deb && \
	rm libtasn1-6_4.14-3_amd64.deb
RUN	wget http://download1.ts3musicbot.net/ffmpeg_4.0-1_amd64-debian9.deb && \ 
	dpkg -i ffmpeg_4.0-1_amd64-debian9.deb && \ 
	rm ffmpeg_4.0-1_amd64-debian9.deb && \ 
	echo "ffmpeg hold"|dpkg --set-selections
RUN apt purge -y apt-utils libapt-inst2.0 && \ 
	find /var/cache -type f -print0 | xargs -0 rm -f && \ 
	rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /usr/share/man/* && \ 
	chown -R root:root /opt/bot/ /etc/init.d/bot && \ 
	chmod -R +x /opt/bot/ /etc/init.d/bot && \ 
	chmod -R 700 /opt/bot/ /etc/init.d/bot && \ 
	update-rc.d bot defaults && \ 
	groupadd -g 1000 ts3mb &&\
	useradd -u 1000 -r -g ts3mb -d /app -s /bin/false -c "Docker image user" ts3mb
	
RUN export DATE_ENV="$DATE_ARG" && \
	export SUM_ENV="$SUM_ARG" && \
	export SOURCE_BRANCH_ENV="$SOURCE_BRANCH_ARG" && \
	export SOURCE_COMMIT_ENV="$SOURCE_COMMIT_ARG" && \
	export DOCKER_REPO_ENV="$DOCKER_REPO_ARG" && \
	export CACHE_TAG_ENV="$CACHE_TAG_ARG" && \
	export IMAGE_NAME_ENV="$IMAGE_NAME_ARG" && \
	echo "docker=1" >> /opt/bot/.env && \ 
	echo "date=\"$DATE_ENV\"" >> /opt/bot/.env && \ 
	echo "branch=\"$SOURCE_BRANCH_ENV\"" >> /opt/bot/.env && \ 
	echo "commit=\"$SOURCE_COMMIT_ENV\"" >> /opt/bot/.env && \ 
	echo "repo=\"$DOCKER_REPO_ENV\"" >> /opt/bot/.env && \ 
	echo "tag=\"$CACHE_TAG_ENV\"" >> /opt/bot/.env && \ 
	echo "image=\"$IMAGE_NAME_ENV\"" >> /opt/bot/.env
	
ADD https://get.aquasec.com/microscanner /
RUN chmod +x /microscanner && \ 
	export MICROSCAN_ENV="$MICROSCAN_ARG" && \ 
	/microscanner $MICROSCAN_ENV --continue-on-failure && \ 
	rm -rf /microscanner


VOLUME /app/ts3mb_core /app/ts3mb_tmp /app/ts3mb_media

ENTRYPOINT ["/opt/bot/entry.sh"]

WORKDIR /app/ts3mb_core
STOPSIGNAL SIGTERM
HEALTHCHECK NONE
HEALTHCHECK --interval=20s --timeout=15s --start-period=15s --retries=3 CMD /opt/bot/health.sh