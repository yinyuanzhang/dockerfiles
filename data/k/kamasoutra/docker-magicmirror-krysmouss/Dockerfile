FROM node:latest

LABEL maintainer="Jean-Pierre Palik - kama@palik.fr" \
      description="MagicMirror personnal image based from bastilimbach/docker-magicmirror" \
      version="1.1"

ENV NODE_ENV production

WORKDIR /opt/magic_mirror

COPY docker-entrypoint.sh /opt

RUN git clone --depth 1 -b master https://github.com/MichMich/MagicMirror.git . && \
    cp -R modules /opt/default_modules && \
    cp -R config /opt/default_config && \
    npm install --unsafe-perm --silent && \
    apt-get update && \
    apt-get -qy install dos2unix && \
    dos2unix /opt/docker-entrypoint.sh && \
    chmod +x /opt/docker-entrypoint.sh && \
    git clone --depth 1 -b master https://github.com/jvanoost/MMM-SNCF.git /opt/magic_mirror/modules/MMM-SNCF && \
    git clone --depth 1 -b master https://github.com/PtrBld/MMM-Scrobbler.git /opt/magic_mirror/modules/MMM-Scrobbler && \
    git clone --depth 1 -b master https://github.com/jasonyork/MMM-auto-refresh.git /opt/magic_mirror/modules/MMM-auto-refresh && \
    git clone --depth 1 -b master https://github.com/MarinescuEvghenii/MMM-QRCode.git /opt/magic_mirror/modules/MMM-QRCode && \
    git clone --depth 1 -b master https://github.com/jclarke0000/MMM-MyCalendar.git /opt/magic_mirror/modules/MMM-MyCalendar

WORKDIR /opt/magic_mirror/modules/MMM-SNCF
RUN npm install

WORKDIR /opt/magic_mirror

EXPOSE 8080
CMD ["node serveronly"]
ENTRYPOINT ["/opt/docker-entrypoint.sh"]
