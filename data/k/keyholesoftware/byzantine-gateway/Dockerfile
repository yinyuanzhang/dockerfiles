FROM node:8-jessie as builder

# ADD APPLICATION TO IMAGE
ADD package*.json /gateway/
ADD *.js /gateway/
ADD app gateway/app

# ADD PEER CREDENTIALS
ADD app/hfc-key-store /home/node/.hfc-key-store

# CHANGE OWNER TO APP DIRECTORY
RUN chown node:node /gateway

# D0N'T RUN AS root
USER node

# WORK IN APP DIRECTORY 
WORKDIR /gateway

# INSTALL RUNTIME DEPENDENCIES
RUN npm install --production

EXPOSE 9090

ENTRYPOINT ["node", "index"]