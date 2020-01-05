FROM hashicorp/middleman-hashicorp:latest as docsbuilder
COPY docs/ .
RUN bundle install && bundle exec middleman build --clean

FROM node:alpine
RUN npm install json-server && npm install --save express-validator
COPY db.1.json ./db.json
COPY server.js ./server.js
COPY --from=docsbuilder /website/build ./public
EXPOSE 3000
ENTRYPOINT ["node", "server.js"]
CMD []
