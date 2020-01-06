FROM node:alpine

ARG EMBER_VERSION=3.12.1
ARG LIVE_RELOAD_PORT=9999
ARG BUILD_DATE

LABEL name="ember-cli ${EMBER_VERSION}" \
	  maintainer="Thomas J. Taylor <thomas@infotechsoft.com>" \
	  build-date="${BUILD_DATE}"

# Add EmberJS
RUN npm install -g ember-cli@${EMBER_VERSION}

EXPOSE 4200 ${LIVE_RELOAD_PORT}
VOLUME /usr/local/ember
WORKDIR /usr/local/ember

ENV PATH=/usr/local/ember/bin:$PATH

# Set the default command:
CMD ["ember", "server", "--live-reload-port", "${LIVE_RELOAD_PORT}"]