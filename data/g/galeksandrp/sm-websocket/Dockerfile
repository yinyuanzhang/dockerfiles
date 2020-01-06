FROM galeksandrp/sm-websocket:docker-1.2-user
USER root
RUN apt-get update && apt-get install -y lib32stdc++6
USER css
WORKDIR /home/css/css/cstrike/addons/sourcemod/scripting
RUN wget --content-disposition https://forums.alliedmods.net/attachment.php?attachmentid=110393
RUN ./spcomp websocket_sourcetv2d.sp -o../plugins/websocket_sourcetv2d.smx
WORKDIR /home/css/css
EXPOSE 12346
