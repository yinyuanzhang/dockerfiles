# Dockerfile for Mission IO Development stack
# Docker, Git, Node, NPM, rimraf, typescript, tslint, mission.cli

FROM docker:latest

RUN apk update \\
    && apk add nodejs --no-cache && node -v \\
    && apk add npm --no-cache && npm -v \\
    && apk add git --no-cache && git version 

RUN npm install mission.cli rimraf typescript tslint mission.shrink -g --ignore-scripts && mio version
