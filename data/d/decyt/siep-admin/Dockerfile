FROM node:alpine
ADD ./webpack /siep-admin/
WORKDIR /siep-admin/

# Descarga el ultimo estado de los commit en los repo developer y master
RUN wget https://api.github.com/repos/MaTiUs77/siep-admin/commits/master && mv master /siep-admin/static/master.json
RUN wget https://api.github.com/repos/MaTiUs77/siep-admin/commits/developer && mv developer /siep-admin/static/developer.json

RUN npm install
CMD ["sh","/siep-admin/docker_init.sh"]

