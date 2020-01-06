# use latest Node LTS (Carbon)
FROM node:carbon

USER root
RUN mkdir /home/node/.npm-global
ENV PATH=/home/node/.npm-global/bin:$PATH
ENV NPM_CONFIG_PREFIX=/home/node/.npm-global

# install Firebase CLI
RUN npm install --unsafe --quiet --no-progress -g @angular/cli@latest firebase-tools