FROM node:8-alpine

# RUN chown -R node:node /usr/local/lib/node_modules \
#   && chown -R node:node /usr/local/bin
RUN npm config set unsafe-perm true
RUN npm i npm@latest -g && npm install -g @angular/cli

# USER root
# RUN ng set --global packageManager=npm
