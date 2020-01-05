FROM node:10.9
LABEL maintainer="camohob <v.samonov@mail.ru>"

# install angular-cli as node user
RUN chown -R node:node /usr/local/lib/node_modules \
  && chown -R node:node /usr/local/bin

USER node
RUN npm install -g @angular/cli@6.1.5

# set npm as default package manager for root
USER root
RUN ng set --global packageManager=npm

# install chromium for headless browser tests
ENV CHROME_BIN=/usr/bin/chromium-browser
RUN apt-get update && apt-get install -y chromium udev ttf-freefont

ENV PROXY_CONF_FILE proxy.conf.json
ENV HOST 0.0.0.0

RUN mkdir -p /app

VOLUME /app
WORKDIR /app

EXPOSE 4200
USER node

CMD ["bash", "-c", "tail -f /dev/null"]