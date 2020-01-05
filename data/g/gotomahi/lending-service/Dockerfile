FROM node:10
WORKDIR /app
COPY package*.json /app/
RUN npm install
COPY ./ /app
EXPOSE 8001
CMD ["node", "--max-old-space-size=128", "server.js"]
