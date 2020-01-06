FROM node:8
LABEL mantainer=ISI-MUITSS
ENV NODE_ENV production
LABEL mantainer=ISI-MUITSS
WORKDIR /sigem-api

COPY package*.json ./
RUN npm install

COPY . .
EXPOSE 80
CMD npm start
