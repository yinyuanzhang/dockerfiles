#Get Windows instance with Node Installed Bambu Specific
#FROM ezrabambu/windowsnode:v1

#NPM Install Package libs
#ADD package.json ./ 
#RUN npm install

#Add all other files to the working directory
#ADD . ./

#WORKDIR ./

#SET ENV To Production
#ENV NODE_ENV=production

#For Windows, take Note it is 'start' and not 'npm start' as the entrypoint is taken as npm
#CMD ["start"]

#For Linux
#CMD ["npm","start"]



#For Linux Instances
FROM node:9-alpine

# Create normal user
# RUN adduser -D normaluser
# USER normaluser

# Create app directory
WORKDIR /app

# Install app dependencies
# A wildcard is used to ensure both package.json AND package-lock.json are copied
# where available (npm@5+)
COPY package*.json ./

RUN npm install
# If you are building your code for production
# RUN npm install --only=production

# Bundle app source
COPY . .

EXPOSE 3000
#SET ENV To Production
ENV NODE_ENV=production

CMD [ "npm", "start" ]