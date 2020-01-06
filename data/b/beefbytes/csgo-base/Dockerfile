FROM beefbytes/steamcmd-base
LABEL maintainer="contact@beefbytes.com"

COPY common/update.sh .
RUN ["bash", "update.sh"]

ENV MAP="de_dust2" \
    MAX_PLAYERS="12" \
    GAMEMODE="0" \
    GAMETYPE="0" \
    MAPGROUP="mg_active" \
    PORT="27015" \
    LOGINTOKEN="" \
    WORKSHOP_AUTHKEY="" \
    WORKSHOP_START_MAP="" \
    WORKSHOP_COLLECTION=""

WORKDIR /home/steam/csgo/
COPY common/start.sh .

CMD ["bash", "start.sh"]
