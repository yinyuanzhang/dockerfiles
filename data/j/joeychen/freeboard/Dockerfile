FROM node:8.9-alpine
LABEL maintainer="joeychen"

RUN apk update && apk add git openssl wget
RUN cd /opt && \
	git clone https://github.com/joeychen/freeboard-plugins.git && \
	git clone https://github.com/joeychen/freeboard-mqtt.git && \
	git clone https://github.com/joeychen/freeboard.git && \		
	cd freeboard && \
	cp -r ../freeboard-plugins/* plugins/ && \
	cp -r ../freeboard-mqtt plugins/mqtt && \	
	npm install grunt http-server -g

RUN cd /opt/freeboard/plugins/mqtt && \
	wget -O mqttws31.js https://cdnjs.cloudflare.com/ajax/libs/paho-mqtt/1.0.1/mqttws31.js

# copy custom demo page 
COPY demo/demo.html /opt/freeboard/ 
COPY demo/board /opt/freeboard/board

RUN cd /opt/freeboard && npm install && grunt 

EXPOSE 80

ENTRYPOINT http-server -p 80 /opt/freeboard

