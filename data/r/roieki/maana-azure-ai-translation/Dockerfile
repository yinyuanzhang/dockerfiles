FROM node:alpine

WORKDIR /app
COPY package.json /app
RUN npm install

#ENV SUBSCRIPTION_KEY=...
ENV AZURE_ENDPOINT=https://api.cognitive.microsofttranslator.com

COPY . /app

CMD npm start

EXPOSE 4000