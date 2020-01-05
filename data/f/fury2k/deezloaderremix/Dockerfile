FROM node:8-alpine

ENV APP_DIR="/app" CONFIG_DIR="/config" PUID="1000" PGID="1000" UMASK="022"

RUN apk add --no-cache git

RUN \
	wget https://notabug.org/RemixDevs/DeezloaderRemix/archive/master.tar.gz && \
	tar -xvf master.tar.gz && \
	rm -rf master.tar.gz && \
        ln -sf /deezloaderremix "${APP_DIR}" && \
	cd "${APP_DIR}" && npm install && npm run dist:linux -- --dir && \
	ln -sf /home/node/.config/Deezloader\ Remix/ "${CONFIG_DIR}"

RUN chown -R  "${PUID}":"${PGID}" "${CONFIG_DIR}" && chown -R   "${PUID}":"${PGID}" "${APP_DIR}"

USER "${PUID}":"${PGID}"

CMD node "${APP_DIR}"/app/app.js

VOLUME "${CONFIG_DIR}" /music

EXPOSE 1730
