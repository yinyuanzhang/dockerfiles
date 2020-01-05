FROM circool/cssds

RUN wget https://mms.alliedmods.net/mmsdrop/1.10/mmsource-1.10.7-git968-linux.tar.gz
RUN wget https://sm.alliedmods.net/smdrop/1.9/sourcemod-1.9.0-git6275-linux.tar.gz
RUN wget http://www.bailopan.net/cssdm/snapshots/2.1/cssdm-2.1.6-git258-linux.tar.gz
RUN tar -C "css/cstrike" -xvzf mmsource-1.10.7-git968-linux.tar.gz
RUN tar -C "css/cstrike" -xvzf sourcemod-1.9.0-git6275-linux.tar.gz
RUN tar -C "css/cstrike" -xvzf cssdm-2.1.6-git258-linux.tar.gz
RUN rm *.gz
# Remove pre-compiled plugins
RUN rm -R /home/steam/css/cstrike/addons/sourcemod/plugins/cssdm

