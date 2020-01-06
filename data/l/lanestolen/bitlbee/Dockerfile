# Setting OS
FROM debian:stretch

# Env
ENV BITLBEEPORT=1337

# install packages
RUN \
    apt-get update &&\
    apt-get install -y --no-install-recommends \
        bitlbee-libpurple git ca-certificates\
        #Used for Facebook
        autoconf automake build-essential libtool libglib2.0-dev libjson-glib-dev bitlbee-dev

# Installing requirements for bitlbee Facebook
RUN \
    git clone https://github.com/bitlbee/bitlbee-facebook.git && \
    cd bitlbee-facebook && \
    ./autogen.sh && \
    make && \
    make install

# Installing requirements for bitlbee Slack
RUN \
    apt install -y --no-install-recommends\
        libpurple-dev && \
    git clone https://github.com/dylex/slack-libpurple.git && \
    cd slack-libpurple && \
    make install

# Expose of ports and volumes
EXPOSE 1337
VOLUME ["/config"]

# Copy folders
COPY root/ /

ENTRYPOINT ["/start.sh"]
