FROM node:8-alpine

# Variables
ARG UID=9999
ARG GID=9999
ENV UID=${UID}
ENV GID=${GID}

# Install packages
RUN addgroup -g ${UID} app && adduser -u ${GID} -G app -D app -s /bin/bash \
    && apk upgrade --update \
    && apk add --no-cache \
       bash bash-completion \
       git curl shadow

# Set working directory
ENV HOME=/home/app/
WORKDIR $HOME

# Bundle APP files
COPY . .
RUN chown -R app:app /home/app/ \
    && chmod -R 755 /home/app/configuration/ \
    && chmod -R 777 /home/app/agent/

USER app
RUN mkdir -p /home/app/.npm-global/bin \
    && npm config set prefix '/home/app/.npm-global' \
    && npm install -g pm2

ENV PATH=/home/app/.npm-global/bin:${PATH}

# Install app dependencies
RUN npm install >/dev/null 2>&1

# Install and configure log-rotate
RUN pm2 install pm2-logrotate >/dev/null 2>&1 \
    && pm2 set pm2-logrotate:max_size 10M >/dev/null 2>&1 \
    && pm2 set pm2-logrotate:compress true >/dev/null 2>&1 \
    && pm2 set pm2-logrotate:retain 7 >/dev/null 2>&1

# Expose the listening port of your app
EXPOSE 9997

# Run node app
CMD ["pm2-runtime", "--env", "development" , "start", "vas.config.js"]
