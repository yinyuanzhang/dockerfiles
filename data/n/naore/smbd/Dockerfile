FROM alpine:latest
LABEL MAINTAINER="naore" \
    Description="Simple and lightweight Samba docker container, based on Alpine Linux." 

# upgrade base system and install samba and supervisord
RUN apk --no-cache upgrade && apk --no-cache add samba samba-common-tools supervisor \

# create a dir for the config and the share
 && mkdir /config /work /mltmedia /doc /p2p /moments /toBsaved \

# add a non-root user and group called "rio" with no password, no home dir, no shell, and gid/uid set to 1000
 && addgroup -g 1000 docker && adduser -D -H -G docker -s /bin/false -u 1000 nas \

# clean cache
 && rm -rf /var/cache/apk/* /tmp/* 
 
# copy config files from project folder to get a default config going for samba and supervisord
COPY *.conf /config/

# create a samba user matching our user from above with a very simple password ("letsdance")
RUN echo -e "love1314\nlove1314" | smbpasswd -a -s -c /config/smb.conf nas

# volume mappings
# VOLUME /config /work /mltmedia /doc /p2p /moments /toBsaved

# exposes samba's default ports (135 for End Point Mapper [DCE/RPC Locator Service],
# 137, 138 for nmbd and 139, 445 for smbd)
EXPOSE 135/tcp 137/udp 138/udp 139/tcp 445/tcp

ENTRYPOINT ["supervisord", "-c", "/config/supervisord.conf"]
