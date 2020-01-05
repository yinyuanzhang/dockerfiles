FROM node:8-alpine

EXPOSE 8000

ENV APP /app
ENV secrets $APP/secrets

WORKDIR $APP

COPY ./package.json $APP
COPY ./package-lock.json $APP

RUN npm install --only=prod

COPY ./src $APP/src

CMD ["npm", "start"]
