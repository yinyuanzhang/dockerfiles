FROM node:argon

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# Fetch the project
COPY . /usr/src/app/my_app
WORKDIR /usr/src/app/my_app/client

RUN npm install -g mocha

EXPOSE 80

CMD ["node", "./bin/www"]