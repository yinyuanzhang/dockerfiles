FROM node:8.11.3-stretch

#create app directory
WORKDIR /usr/src/app

# Install app dependencies
COPY package.json .



ARG NPM_TOKEN
COPY .npmrc .npmrc

RUN npm install

#Bundle app source
COPY . .

#TODO: install a bunch of other software such as logging, etc. this will need ot be built into the service as well


#Exposing port
#This part is tricky, because with multiple services, we'll want to have different ports for different services
#It might be ideal to assume any service is running in docker, and have them all auto-expose 8080. Then have the cli
#auto-assign the port mapping to that docker image. When developing on multiple microservices, however, that might
#not be ideal, we may need to build it into a docker file every time its ran, which would be bad.

#Maybe have a dev config file or flag and if specified to 'dev', exposes a custom port (or jsut a dev-port flag)

CMD [ "node", "app.js" ]
