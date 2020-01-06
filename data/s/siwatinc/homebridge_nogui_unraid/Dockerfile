FROM siwatinc/nodejsubuntu_base_image
RUN npm install -g --unsafe-perm homebridge
RUN apt-get update --fix-missing
RUN apt-get -y install wget git
CMD apt-get update && apt-get -y install $aptpackages || : && npm install -g --unsafe-perm $packages && homebridge -I
