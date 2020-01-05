FROM node:alpine

ENV PRISMA_SECRET supersecret 
ENV PRISMA_ENDPOINT http://localhost:4466 

WORKDIR /usr/src/app

COPY package*.json ./
RUN npm install

COPY . .

EXPOSE 4000 
CMD [ "npm", "start" ]