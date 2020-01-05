FROM node:alpine

EXPOSE 8100
ENV ISSUER=http://localhost:8100

WORKDIR /app

COPY ./ ./

RUN npm install

CMD node ./bin/oauth2-mock-server -p 8100