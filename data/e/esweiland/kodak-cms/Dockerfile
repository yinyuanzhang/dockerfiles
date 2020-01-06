# Dockerfile is used by Docker to build the Docker image
# docker build -t <container_name> .
# For this project docker build -t kodak-cms .
# Ignored when starting the app directly (i.e. $ node app.js)
# Provides node.js to the project
FROM node:latest

# Create app directory
RUN mkdir -p /app
WORKDIR /app

# Bundle app source
COPY . /app
RUN npm install

# Mount persistent storage
# VOLUME /<host directory>:/<vm direcctoy> # map host to vm
# VOLUME <vm directory>
VOLUME /app/data
VOLUME /app/public/uploads

#Environment Variables
#ENV MONGODB_PORT_27017_TCP_ADDR='mongodb://mongo'
#ENV MONGODB_PORT_27017_TCP_PORT='27017'
#ENV APOS_MONGODB_URI  "mongodb://mongo:27017/kodak-cms"
#ENV APOS_ALWAYS_COPY_ASSETS=1

EXPOSE 3000
#CMD [ "npm", "start" ]
CMD [ "node", "app.js" ]
