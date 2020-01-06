FROM        node:0.12

# grab gosu for easy step-down from root
RUN gpg --keyserver ha.pool.sks-keyservers.net --recv-keys B42F6819007F00F88E364FD4036A9C25BF357DD4
RUN arch="$(dpkg --print-architecture)" \
	&& set -x \
	&& curl -o /usr/local/bin/gosu -fSL "https://github.com/tianon/gosu/releases/download/1.3/gosu-$arch" \
	&& curl -o /usr/local/bin/gosu.asc -fSL "https://github.com/tianon/gosu/releases/download/1.3/gosu-$arch.asc" \
	&& gpg --verify /usr/local/bin/gosu.asc \
	&& rm /usr/local/bin/gosu.asc \
	&& chmod +x /usr/local/bin/gosu

RUN	        npm install -g grunt-cli grunt

# Install player app
COPY        bin /opt/player/bin
COPY        www /opt/player/www
COPY        views /opt/player/views
COPY        test /opt/player/test
COPY        *.js /opt/player/
COPY        *.json /opt/player/
COPY        env.ini /opt/player/
COPY        Procfile /opt/player/
RUN	        cd /opt/player && npm install && grunt setup 

# add our user and group first to make sure their IDs get assigned consistently, regardless of whatever dependencies get added
RUN         groupadd -r player && useradd -r -g player player

COPY        docker-entrypoint.sh /

WORKDIR     /opt/player

ENTRYPOINT ["/docker-entrypoint.sh"]

EXPOSE      8080

CMD         ["grunt", "www"]