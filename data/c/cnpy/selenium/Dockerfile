FROM elgalu/selenium:latest

RUN sudo apt-get update -qq && \
	sudo apt-get install -y thunar && \
	sudo apt-get clean && \
	sudo rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

COPY images/wallpaper-canopy.png /usr/share/images/fluxbox/ubuntu-light.png
COPY images/wallpaper-canopy.png /usr/share/images/fluxbox/wallpaper-zalenium.png

CMD ["entry.sh"]
