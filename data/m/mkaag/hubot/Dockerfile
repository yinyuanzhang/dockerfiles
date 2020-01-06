FROM node:0.12-slim
MAINTAINER Maurice Kaag <mkaag@me.com>

# -----------------------------------------------------------------------------
# Environment variables
# -----------------------------------------------------------------------------
ENV HUBOT_NAME hubot
ENV HUBOT_SLACK_TOKEN false
ENV HUBOT_AUTH_ADMIN myself
ENV GITLAB_CHANNEL general
ENV GITLAB_DEBUG false
ENV GITLAB_BRANCHES master
ENV GITLAB_SHOW_COMMITS_LIST 0
ENV GITLAB_SHOW_MERGE_DESCRIPTION 0
ENV HUBOT_NEWRELIC_API_KEY false
ENV HUBOT_NEWRELIC_API_HOST api.newrelic.com

# -----------------------------------------------------------------------------
# Pre-install
# -----------------------------------------------------------------------------
ADD build/ /opt/
WORKDIR /opt

# -----------------------------------------------------------------------------
# Install
# -----------------------------------------------------------------------------
RUN npm install --production; npm cache clean

# -----------------------------------------------------------------------------
# Post-install
# -----------------------------------------------------------------------------
EXPOSE 8080
VOLUME /opt/scripts

CMD ["/opt/bin/hubot", "--name", "${HUBOT_NAME}", "--adapter", "slack"]