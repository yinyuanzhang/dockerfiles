FROM node:10.13-alpine

ENV PUID 1001
ENV PGID 1001
ENV PUSER flood
ENV PGROUP data
ENV FLOOD_DIR /flood/
ENV FLOOD_SECRET wmtsflumfyegcclx

RUN apk add --no-cache --virtual=build-dependencies git python build-base && \
	apk add --no-cache --upgrade curl mediainfo nano tar wget shadow su-exec && \
	rm -rf /root/.cache /tmp/* && \
	addgroup -g $PGID $PGROUP && \
	adduser -D -G $PGROUP -u $PUID $PUSER && \
	git clone https://github.com/jfurrow/flood.git

WORKDIR $FLOOD_DIR

RUN npm install && \
	npm cache clean --force

COPY root /

RUN chmod +x /usr/local/bin/docker-entrypoint.sh && \
	npm run build && \
	npm prune --production && \
	apk del --purge build-dependencies	

EXPOSE 3000

ENTRYPOINT ["/usr/local/bin/docker-entrypoint.sh"]

CMD ["npm", "start"]
