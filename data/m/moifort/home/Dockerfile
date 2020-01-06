FROM node:10.9.0-alpine

RUN mkdir -p /app
COPY . /app
WORKDIR /app


COPY package.json /app
#RUN npm rebuild
RUN npm install

ENV NODE_ENV=production

COPY . /app
RUN npm run build

ENV HOST 0.0.0.0
EXPOSE 3000

CMD ["npm", "start"]
