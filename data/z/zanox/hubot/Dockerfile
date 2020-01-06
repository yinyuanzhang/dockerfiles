FROM debian
MAINTAINER Paul Turner <paul.turner@affiliatewindow.com>

RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -yqq \
    curl nodejs nodejs-legacy npm && \
    apt-get clean && rm -r /var/lib/apt/lists/*

RUN npm install -g yo generator-hubot

WORKDIR /hubot
RUN groupadd -r hubot && useradd -r -g hubot hubot --home /hubot && chown hubot:hubot /hubot
USER hubot

RUN npm install hubot-trollbot hubot-weather
RUN yes | yo hubot --owner="Paul Turner <paul.turner@affiliatewindow.com>" --name="Hubot" --adapter=irc --defaults


ENV HUBOT_IRC_SERVER=irc.freenode.net
ENV HUBOT_IRC_ROOMS="#zanox-hubot"
ENV HUBOT_IRC_NICK="zubot"
ENV HUBOT_IRC_UNFLOOD="true"

CMD ["./bin/hubot", "-a", "irc"]
