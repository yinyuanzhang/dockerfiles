# Create image based on the official Node 8 image from dockerhub
FROM node:9.6.1 as builder

# Create a directory where our app will be placed
RUN mkdir /app

# Change directory so that our commands run inside this new directory
WORKDIR /app

# Copy dependency definitions
COPY package.json package-lock.json /app/
RUN npm install -g @angular/cli@6.1.5 -g
# Install dependecies
RUN cd /app && npm install
COPY ./  /app/

ARG FRONT_ENVIRONMENT=local
# Build with $env variable from outside
RUN cd /app && npm run build:$FRONT_ENVIRONMENT
RUN ls /app/dist
#ENTRYPOINT npm start

# Expose the port the app runs in
#EXPOSE 8080/tcp

# Serve the app
#CMD ["npm", "start"]

###################
#### production ###
###################
# base image
FROM bitnami/nginx
COPY nginx.conf /opt/bitnami/nginx/conf/nginx.conf
COPY --from=builder /app/dist/. /opt/bitnami/nginx/html
#RUN mkdir /opt/bitnami/nginx/tmp
#RUN mkdir /opt/bitnami/nginx/tmp/client_body
#RUN chmod -R a+rwx /opt/bitnami/nginx/tmp
#
## expose port 80
EXPOSE 8080
##
# run nginx
CMD ["nginx", "-g", "daemon off;"]