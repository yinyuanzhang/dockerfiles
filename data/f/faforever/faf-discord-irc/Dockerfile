FROM node:7.4.0

# Get discord-irc
RUN mkdir /discord-irc
WORKDIR /discord-irc
RUN curl -L https://github.com/FAForever/discord-irc/tarball/master | tar -xz --strip-components 1
RUN npm install
RUN npm run build

CMD cd /discord-irc && npm start -- --config /config/config.json
