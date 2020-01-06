FROM node:10

RUN apt-get update && apt-get install -y \
    wakeonlan \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY package*.json /app/
RUN npm install

COPY *.js /app/
CMD [ "npm", "start" ]
