FROM siwatinc/nodejsubuntu_base_image
EXPOSE 3006
RUN apt-get update --fix-missing
RUN apt-get update 
RUN wget https://github.com/marcelveldt/roon-extension-api-proxy/archive/master.zip -O /master.zip 
WORKDIR /
RUN unzip master.zip -d /roon-api
WORKDIR /roon-api/roon-extension-api-proxy-master
RUN npm install
CMD node .
