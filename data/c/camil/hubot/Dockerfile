FROM node:latest
MAINTAINER Camil Blanaru <camil@edka.io>

# Usual update / upgrade
ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update && apt-get upgrade -y && apt-get dist-upgrade -y && \
        apt-get install -y redis-server git-core
# Clean up APT when done
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Install coffee-script, hubot
RUN npm install -g yo generator-hubot coffee-script

# Working enviroment
ENV BOTDIR /opt/bot
RUN install -o nobody -d ${BOTDIR}
ENV HOME ${BOTDIR}
WORKDIR ${BOTDIR}

# Install Hubot
USER nobody
RUN yo hubot --name="Hubot" --defaults

# Install slack adapter
RUN npm install hubot-slack --save

#Install Redmine adapter
RUN npm install hubot-redmine --save

# Install cleverbot
RUN npm install cleverbot-node --save
ADD scripts/cleverbot.coffee ${BOTDIR}/scripts/cleverbot.coffee
ADD scripts/cleverbot.coffee ${BOTDIR}/scripts/credmine.coffee

# Entrypoint
ENTRYPOINT ["/bin/sh", "-c", "cd ${BOTDIR} && bin/hubot --adapter slack"]
