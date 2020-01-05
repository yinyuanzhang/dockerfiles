FROM node:9.11.1-alpine


# TODO: Convert this Dockerfile to use multistage builds
# (image size is currently 277MB, see how small it can get)


# The base node image sets a very verbose log level.
ENV NPM_CONFIG_LOGLEVEL warn
ENV PORT=3000

# Copy all local files into the image.
COPY . /var/www
WORKDIR /var/www

# Install `serve` to run the application.
RUN npm install

# Tell Docker about the port we'll run on.
EXPOSE $PORT

# Set the command to start the node server.
ENTRYPOINT [ "npm", "start" ]
