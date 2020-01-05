FROM node:latest

COPY . /usr/src/sitiopersonal
WORKDIR /usr/src/sitiopersonal

RUN npm install --production
ENV NODE_ENV production

ENV PORT 3000

EXPOSE 3000

CMD ["npm", "start"]