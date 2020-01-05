FROM milf/steamcmd

LABEL maintainer="marcrominger@gmx.de"

ENV STEAMAPPID 739590
ENV STEAMAPPDIR /home/steam/eco-dedicated

ENV IDK_PORT=2999
ENV GS_PORT=3000
ENV WS_PORT=3001

RUN mkdir ${STEAMAPPDIR}

RUN set -x \
	&& "${STEAMDIR}/steamcmd.sh" \
		+login anonymous \
		+force_install_dir ${STEAMAPPDIR} \
		+app_update ${STEAMAPPID} validate \
		+quit

WORKDIR $STEAMAPPDIR

VOLUME $STEAMAPPDIR

ENTRYPOINT ${STEAMDIR}/steamcmd.sh \
		+login anonymous +force_install_dir ${STEAMAPPDIR} +app_update ${STEAMAPPID} +quit \
		&& ${STEAMAPPDIR}/EcoServer.sh -nogui 


EXPOSE ${IDK_PORT}
EXPOSE ${GS_PORT}
EXPOSE ${WS_PORT}
