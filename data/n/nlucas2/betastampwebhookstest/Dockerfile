FROM node:10.9-alpine
workdir /app

COPY package*.json ./
RUN npm install
COPY . .

EXPOSE 8081
CMD ["node", "index.js"]

