# Dockerfile for Garry's Mod server

# Use the official steamcmd image
FROM cm2network/steamcmd

# Update steam, install Garry's Mod Server and download Counter Strike Source files
RUN ./home/steam/steamcmd/steamcmd.sh +login anonymous +force_install_dir "/home/steam/gmod" +app_update 4020 validate +force_install_dir "/home/steam/css" +app_update 232330 +quit

# Add mount config so GMod can find CSS files
RUN printf '"mountcfg"\n{\n"cstrike" "/home/steam/css/cstrike"\n}\n' > /home/steam/gmod/garrysmod/cfg/mount.cfg

# Expose Ports
EXPOSE 27005 27015

# Set environment variables so player count, startup map and steam workshop collection can easily be changed by the 'docker run' command
ENV MAX_PLAYERS=16
ENV START_MAP=ttt_bb_teenroom_b2
ENV GAME_MODE=terrortown
ENV COLLECTION=298502203
ENV HOSTNAME='TTT-Server powered by Docker'
ENV SERVER_PASSWORD=
ENV ADMIN_NAME=garry
ENV ADMIN_ID=STEAM_0:1:7099

# Set Hostname and Serverpassword
RUN printf "hostname \"${HOSTNAME}\"\nsv_password \"${SERVER_PASSWORD}" > /home/steam/gmod/garrysmod/cfg/server.cfg

# Set Server Admin
RUN printf "\"Users\"\n{\n\"superadmin\"\n{\n\"${ADMIN_NAME}\" \"${ADMIN_ID}\"\n}\n\"admin\"\n{\n\"${ADMIN_NAME}\" \"${ADMIN_ID}\"\n}\n}" > /home/steam/gmod/garrysmod/settings/users.txt

# Entrypoint
ENTRYPOINT ./home/steam/gmod/srcds_run -console -game garrysmod +maxplayers ${MAX_PLAYERS} +map ${START_MAP} +gamemode ${GAME_MODE} +host_workshop_collection ${COLLECTION}
