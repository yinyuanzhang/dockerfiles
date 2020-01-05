FROM docker:latest

RUN apk add --update nodejs yarn

ENV HEROKU_CLI_VERSION '7.25.0'
RUN yarn global add heroku@$HEROKU_CLI_VERSION

CMD ["heroku"]
