FROM node:latest

# Who to contact with questions
MAINTAINER siggame@mst.edu

# Create a user named siggame with a home directory but no login shell
RUN useradd --user-group --create-home --shell /sbin/nologin siggame

# Set the home environment variable
ENV HOME /home/siggame

# Set which port(s) are exposed for the container
EXPOSE 3001

# Set the environment variable to let node know its in a production setting
# This will enable caching in express among other things. For a dev environment,
# override this with -e NODE_ENV="development"
ENV NODE_ENV production

# Copy over the package.json file
COPY package.json $HOME/ophelia/

# Change the ownership of everything in siggame's home to siggame
RUN chown -R siggame:siggame $HOME/*

# Change to the siggame user
USER siggame
# Set the work directory to the ophelia directory
WORKDIR $HOME/ophelia
# Install the webserver's dependencies in the workdir
RUN npm install

# Change back to the root user
USER root
# Copy all of the webserver code into the ophelia directory except for things
# excluded in .dockerignore
COPY . .
# Change ownership of everything in ophelia directory to siggame user
RUN chown -R siggame:siggame $HOME/ophelia/*
# Change back to the siggame user
USER siggame

# Start the server by executing npm start
CMD [ "npm", "start" ]
