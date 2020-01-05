FROM node:10.16-stretch

ENV ANGULAR_CLI_VERSION=8.3.20

# Install angular-cli
RUN chown -R node:node /usr/local/lib/node_modules \
 && chown -R node:node /usr/local/bin
USER node
RUN npm install -g @angular/cli@"$ANGULAR_CLI_VERSION" \
 && ng version

# Install chromium for headless browser tests
USER root
RUN apt-get update \
 && apt-get install -y --no-install-recommends chromium \
 && apt-get autoremove -y \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \
 && /usr/bin/chromium --version
ENV CHROME_BIN=/usr/bin/chromium

# Run configuration
WORKDIR /app
USER node
ENTRYPOINT ["ng"]
CMD ["version"]
