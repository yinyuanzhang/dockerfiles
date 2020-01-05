# https://github.com/chihchun/hubot-slack-docker
FROM node:6

# Software versions
ENV HUBOT_SLACK_VERSION=4.0.5
ENV HUBOT_VERSION=0.4.0
ENV YO_VERSION=1.8.5
ENV COFFEE_SCRIPT=1.10.0
#ENV MONGODB_VERSION=2.2.28

# Usual update / upgrade
ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update \
 && apt-get install -y jq

# Clean up APT when done
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Install coffee-script, hubot, mongodb
RUN npm install -g yo@${YO_VERSION} \
        coffee-script@${COFFEE_SCRIPT} \
        generator-hubot@${HUBOT_VERSION}
#        mongodb@${MONGODB_VERSION}

# Working enviroment
ENV BOTDIR /opt/bot
RUN install -o nobody -d ${BOTDIR}

WORKDIR ${BOTDIR}

# Install Hubot
USER nobody
ENV HOME ${BOTDIR}
RUN yo hubot --name="Hubot" --defaults

# Install slack adapter
RUN npm install hubot-slack@${HUBOT_SLACK_VERSION} --save

# Install moretext
RUN npm install moretext@1.0.0 --save
ADD scripts/moretext.coffee ${BOTDIR}/scripts/moretext.coffee

# Install hubot-victory  https://github.com/hubot-scripts/hubot-victory
RUN npm install hubot-victory@1.5.3 \
 && (cat external-scripts.json && echo '["hubot-victory"]') | jq -s add > external-scripts.json.new \
 && mv external-scripts.json.new external-scripts.json

# Install hubot-healthcheck
ENV HUBOT_NOTIFICATIONS_ROOM \#builds
ADD scripts/healthcheck.js ${BOTDIR}/scripts/healthcheck.js

# Entrypoint
CMD ["/bin/sh", "-c", "cd ${BOTDIR} && bin/hubot --adapter slack"]