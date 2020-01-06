FROM node:8.7.0

RUN npm install npm@latest && \
    rm -rf /usr/local/lib/node_modules/npm && \
    mv node_modules/npm /usr/local/lib/node_modules/npm && \
    npm install -g sails

WORKDIR /home/node/app
CMD sails lift
