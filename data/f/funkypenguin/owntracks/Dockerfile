FROM debian:jessie
LABEL version="0.4" description="Mosquitto and OwnTracks Recorder"
LABEL authors="Jan-Piet Mens <jpmens@gmail.com>, Giovanni Angoli <juzam76@gmail.com>"

# BUILD_DATE and VCS_REF are immaterial, since this is a 2-stage build, but our build
# hook won't work unless we specify the args
ARG BUILD_DATE
ARG VCS_REF

# Good docker practice, plus we get microbadger badges
LABEL org.label-schema.build-date=$BUILD_DATE \
      org.label-schema.vcs-url="https://github.com/funkypenguin/recorderd.git" \
      org.label-schema.vcs-ref=$VCS_REF \
      org.label-schema.schema-version="2.2-r1"


ADD http://repo.owntracks.org/repo.owntracks.org.gpg.key /tmp/owntracks.gpg.key
ADD http://repo.mosquitto.org/debian/mosquitto-repo.gpg.key /tmp/mosquitto.gpg.key

RUN	apt-key add /tmp/owntracks.gpg.key && \
	apt-key add /tmp/mosquitto.gpg.key && \
	apt-get update && \
	apt-get install -y software-properties-common net-tools && \
	apt-add-repository 'deb http://repo.owntracks.org/debian jessie main' && \
	apt-add-repository 'deb http://repo.mosquitto.org/debian jessie main' && \
	apt-get update && \
	apt-get install -y \
		libmosquitto1 \
		libsodium13 \
		libcurl3 \
		liblua5.2-0 \
		mosquitto \
		mosquitto-clients \
		supervisor \
		ot-recorder \
		curl \
		&& \
	apt-get clean && \
	rm -rf /var/lib/apt/lists/*

# data volume
VOLUME /owntracks

COPY ot-recorder.default /etc/default/ot-recorder

COPY launcher.sh /usr/local/sbin/launcher.sh
COPY generate-CA.sh /usr/local/sbin/generate-CA.sh

COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf
COPY mosquitto.conf mosquitto.acl /etc/mosquitto/

COPY recorder-health.sh /usr/local/sbin/recorder-health.sh

# Disabled this, because it's breaking password-only access
#HEALTHCHECK CMD /usr/local/sbin/recorder-health.sh

RUN mkdir -p /var/log/supervisor && \
	mkdir -p -m 775 /owntracks/recorder/store && \
	chown -R owntracks:owntracks /owntracks && \
	chmod 755 /usr/local/sbin/launcher.sh /usr/local/sbin/generate-CA.sh /usr/local/sbin/recorder-health.sh

EXPOSE 1883 8883 8083
CMD ["/usr/local/sbin/launcher.sh"]
