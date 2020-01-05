FROM geodata/gdal:2.1.3
MAINTAINER Jörg Herbst <joerg.herbst@10m.de>

RUN add-apt-repository -y ppa:chris-lea/node.js
RUN apt-get -y update
RUN apt-get -y install nodejs
RUN npm install -g ogre@1.2.0

EXPOSE 3000
CMD ogre
