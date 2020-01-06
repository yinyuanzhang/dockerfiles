FROM debian:stable-slim

LABEL "maintainer"="nodefortytwo <github@rickburgess.me>"
LABEL "repository"="https://github.com/nodefortytwo/gha-wait-for-deployment"

LABEL "com.github.actions.name"="Wait for deployment"
LABEL "com.github.actions.description"="Poll a URL until it returns a desired value"
LABEL "com.github.actions.icon"="refresh-cw"
LABEL "com.github.actions.color"="blue"

RUN apt-get update && apt-get install -y curl jq

ADD entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["sh", "/entrypoint.sh"]