FROM node:10-alpine
RUN mkdir -p /app
WORKDIR /app
COPY package*.json ./
RUN npm install --only=production
COPY . .
EXPOSE 80

CMD ["npm", "run", "start"]