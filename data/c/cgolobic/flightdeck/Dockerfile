FROM node:10.15-alpine
RUN npm -g config set user root

WORKDIR /usr/src/app

RUN npm install -g @angular/cli@latest

# copy the contents of the local project dir to the working dir of the container 
# (excluding files/dirs listed in .dockerignore)
COPY . .

WORKDIR /usr/src/app/flightdeck-client
RUN npm install


WORKDIR /usr/src/app/flightdeck-server
RUN npm install

ENV NODE_ENV production
EXPOSE 3000
CMD npm run start:prod