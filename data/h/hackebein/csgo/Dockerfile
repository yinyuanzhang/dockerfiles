FROM hackebein/srcds

ENV \
	# App
	APPS="740" \
	#
	# API
	# http://steamcommunity.com/dev/apikey
	AUTHKEY="" \
	#
	# Public access
	# automatic via API
	GLSTAPP="730" \
	# manual
	# APPID: 730
	# http://steamcommunity.com/dev/managegameservers
	GLST="" \
	#
	# Workshop (require API)
	WORKSHOPCOLLECTIONID="" \
	#
	# Server config
	TICKRATE="128" \
	MAXPLAYERS="16" \
	GAMEMODE="0" \
	GAMETYPE="0" \
	MAP="de_mirage" \
	MAPGROUP="mg_active" \
	CONFIG="server.cfg" \
	#
	# Other
	CUSTOMPARAMETERS="" \
	#
	# Start parameters
	SRCDSPARAMS="\
		-game csgo \
		-usercon \
		-nobreakpad \
		-tickrate \${TICKRATE} \
		-maxplayers \${MAXPLAYERS} \
		-authkey \${AUTHKEY} \
		+host_workshop_collection \${WORKSHOPCOLLECTIONID} \
		+workshop_start_map \
		+game_mode \${GAMEMODE} \
		+game_type \${GAMETYPE} \
		+map \${MAP} \
		+mapgroup \${MAPGROUP} \
		+servercfgfile \${CONFIG} \
		\${CUSTOMPARAMETERS} \
	"
