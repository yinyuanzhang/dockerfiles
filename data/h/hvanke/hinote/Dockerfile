FROM node:8.12.0-alpine

WORKDIR /app

COPY . /app
RUN yarn --pure-lockfile

EXPOSE 3000

CMD ["npm", "run", "start"]
