FROM node:8

WORKDIR /app
COPY package.json /app/package.json
COPY package-lock.json /app/package-lock.json

COPY src /app/src
COPY app.js /app/app.js
COPY index.html /app/index.html

RUN npm install

ENTRYPOINT ["/bin/bash", "-c", "nodejs /app/app.js"]
