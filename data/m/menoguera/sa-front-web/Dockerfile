# Installs the current application on a Node Image.
FROM node:8-alpine
# The qq is for silent output in the console
# You are welcome to modify this part as it

# Sets the path where the app is going to be installed
ENV NODE_ROOT /usr/app/
# Creates the directory and all the parents (if they don’t exist)
RUN mkdir -p $NODE_ROOT
# Sets the /usr/app as the active directory
WORKDIR $NODE_ROOT
# Copies all the content
COPY . .
# Install all the packages
RUN npm install -g @angular/cli
RUN yarn install

# The default port from ng serve (4200)
# and 49153 for Webpack Hot Module Reload
EXPOSE 4200 49153
