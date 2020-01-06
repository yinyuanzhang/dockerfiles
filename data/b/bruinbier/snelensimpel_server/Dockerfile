FROM node:10-alpine
RUN mkdir -p /home/node/app1/node_modules && chown -R node:node /home/node/app1
WORKDIR /home/node/app1
COPY package*.json ./
RUN npm install
COPY . .
COPY --chown=node:node . .
EXPOSE 8081

CMD [ "node", "src/app.js" ]