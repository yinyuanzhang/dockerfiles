FROM lsiobase/alpine:3.9
EXPOSE 1730
RUN \
	apk add --no-cache --upgrade \
	wget \
	bash \
	unzip \
	git \
	nodejs-npm \
	yarn
RUN \	
	wget https://notabug.org/RemixDevs/DeezloaderRemix/archive/master.zip && \
	unzip master.zip -d /app && \
	mv /app/deezloaderremix/* /app && \
	rm -r /app/deezloaderremix &&  \
	rm master.zip
COPY authCredentials.js /app
COPY localpaths.js /app/app/utils
WORKDIR /app
RUN chown -R abc:abc /app
RUN mkdir -p /home/abc/.config/DeezloaderRemix/logs
RUN chown -R abc:abc /home/abc/
RUN yarn install
COPY root/ /
VOLUME ["/home/abc/music", "/home/abc/.config/DeezloaderRemix"]
