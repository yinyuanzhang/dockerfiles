FROM laynal/docker-css-server

# Install plugins
RUN wget -O /home/steam/sm_ggdm.zip "https://forums.alliedmods.net/attachment.php?attachmentid=108943&d=1346584450" && \
	unzip -o /home/steam/sm_ggdm.zip -d /home/steam/css-dedicated/cstrike && \
	rm /home/steam/sm_ggdm.zip && \
	wget -O /home/steam/sm_gungame.zip "https://forums.alliedmods.net/attachment.php?s=716ef65609b491b4a34670e767887027&attachmentid=133712&d=1400696532" && \
	unzip -o /home/steam/sm_gungame.zip -d /home/steam/css-dedicated/cstrike && \
	rm /home/steam/sm_gungame.zip && \
	mv /home/steam/css-dedicated/cstrike/addons/sourcemod/plugins/gungame.smx /home/steam/css-dedicated/cstrike/addons/sourcemod/plugins/disabled/ && \
	mv /home/steam/css-dedicated/cstrike/addons/sourcemod/plugins/disabled/gungame_sdkhooks.smx /home/steam/css-dedicated/cstrike/addons/sourcemod/plugins/

# Start server with basic settings. Add arguments as needed
CMD /home/steam/css-dedicated/srcds_run -game cstrike -console +map cs_italy
