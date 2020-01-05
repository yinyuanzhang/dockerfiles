FROM node:10.15.3-alpine 

WORKDIR /app
COPY package.json package-lock.json ./
RUN npm install --production

COPY src ./src
RUN chmod +x ./src/server.js

ENV NODE_ENV=production \
    SHUTDOWN_TIME="0 0 18 * * *" \
    TZ=America/Los_Angeles

CMD ["npm", "start"]