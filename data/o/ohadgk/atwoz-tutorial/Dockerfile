# This image will be based on the official nodejs docker image
FROM node:latest
 
# Set in what directory commands will run
WORKDIR /home/app
 
# Put all our code inside that directory that lives in the container
ADD . /home/app
 
# Install dependencies
RUN \
    npm install -g tsd && \
    npm install -g webpack && \
    npm install && \
    webpack
    


EXPOSE 8080
 
# The command to run our app when the container is run
CMD ["node", "server/app.js"]