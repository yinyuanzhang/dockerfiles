# Dockerfile
FROM  debian:buster-slim

LABEL maintainer="RogueThorn"
LABEL description="Utopia Mining Image"

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
	apt install -y --no-install-recommends ca-certificates apt-utils wget screen nano libslang2 libglib2.0-0


RUN apt purge -y apt-utils libapt-inst2.0 && \ 
	find /var/cache -type f -print0 | xargs -0 rm -f && \ 
	rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /usr/share/man/* && \ 
	chown -R root:root /opt/bot/ /etc/init.d/bot && \ 
	chmod -R +x /opt/bot/ /etc/init.d/bot && \ 
	chmod -R 700 /opt/bot/ /etc/init.d/bot && \ 
	update-rc.d bot defaults && \ 
	groupadd -g 1000 utopia &&\
	useradd -u 1000 -r -g utopia -d /app -s /bin/false -c "Docker image user" utopia
	
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


VOLUME /app/

ENTRYPOINT ["/opt/bot/entry.sh"]

WORKDIR /app/
STOPSIGNAL SIGTERM
#HEALTHCHECK NONE
#HEALTHCHECK --interval=20s --timeout=15s --start-period=15s --retries=3 CMD /opt/bot/health.sh