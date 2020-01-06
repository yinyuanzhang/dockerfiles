FROM beefbytes/csgo-base
LABEL maintainer="contact@beefbytes.com"

WORKDIR /home/steam/csgo/csgo/

# Sourcemod
RUN wget -O sourcemod.tar.gz https://sm.alliedmods.net/smdrop/1.9/sourcemod-1.9.0-git6245-linux.tar.gz \
    && tar -xvzf sourcemod.tar.gz \
    && rm sourcemod.tar.gz

# Metamod
RUN wget -O metamod.tar.gz https://mms.alliedmods.net/mmsdrop/1.10/mmsource-1.10.7-git963-linux.tar.gz \
    && tar -xvzf metamod.tar.gz \
    && rm metamod.tar.gz

ENV MAP="de_dust2" \
    MAX_PLAYERS="12" \
    GAMEMODE="0" \
    GAMETYPE="0" \
    MAPGROUP="mg_active" \
    PORT="27015" \
    LOGINTOKEN=""

WORKDIR /home/steam/csgo/

CMD ["bash", "start.sh"]
