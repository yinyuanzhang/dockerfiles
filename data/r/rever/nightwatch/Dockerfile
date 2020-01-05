#
# Nightwatch.js Dockerfile
#

FROM node:10.16.0-jessie

RUN apt-get update \
  && apt-get install -y libnss3 \
  && npm install -g \
  npm@latest \
  nightwatch@'<1.1.12' \
  nightwatch-video-recorder@^3.0.0 \
  # Clean up obsolete files:
  && rm -rf \
  /tmp/* \
  /root/.npm

# Set NODE_PATH to be able to require globally installed packages:
ENV NODE_PATH=/usr/lib/node_modules

# Avoid permission issues with host mounts by assigning a user/group with
# uid/gid 1000 (usually the ID of the first user account on GNU/Linux):
RUN mkdir -p /home/nightwatch/reports && chmod -R 777 /home/nightwatch/reports
RUN adduser -u 10000 nightwatch

RUN chmod -R 777 /home/nightwatch

USER nightwatch
WORKDIR /home/nightwatch

COPY wait-for.sh /usr/local/bin/wait-for

ENTRYPOINT ["wait-for", "--", "nightwatch"]
