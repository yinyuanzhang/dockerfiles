FROM siwatinc/nodejsubuntu_base_image
RUN npm install -g dmx-hue
CMD dmx-hue setup -i $huebridgeip | : && dmx-hue -a $dmxaddress -u $artnetuniverse -t $transition -c
