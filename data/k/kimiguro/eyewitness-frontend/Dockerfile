FROM mhart/alpine-node:latest

WORKDIR /app
COPY ./frontend/package*.json ./

RUN npm install

COPY ./frontend .

EXPOSE 80
CMD ["npm", "run", "prod"]