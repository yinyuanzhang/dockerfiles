FROM alpine:3.8
LABEL maintainer "s7b4 <baron.stephane@gmail.com>"

# Minecraft
ENV APP_USER=minecraft
ENV APP_HOME=/home/$APP_USER

# set user/group IDs
RUN addgroup $APP_USER && \
	adduser -G $APP_USER -D -H -s /bin/bash -h $APP_HOME $APP_USER

# Base
RUN apk --no-cache add bash \
		curl \
		su-exec \
		openjdk8-jre-base

# Minecraft
RUN mkdir -p /opt/minecraft \
	&& curl -o /opt/minecraft/minecraft_server.jar -sSL "https://launcher.mojang.com/v1/objects/d0d0fe2b1dc6ab4c65554cb734270872b72dadd6/server.jar"

COPY scripts/entrypoint.sh /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]

EXPOSE 25565 25575
VOLUME $APP_HOME
