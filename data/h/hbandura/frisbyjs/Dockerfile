FROM node:lts-slim
RUN npm install -g frisby
RUN npm install -g jasmine-node
RUN npm install -g jest
ENV NODE_PATH /usr/local/lib/node_modules/
ADD jest.config.js /workdir/jest.config.js
WORKDIR /workdir
VOLUME ["/workdir", "/workdir/__tests__"]
ENTRYPOINT [ "jest" ]