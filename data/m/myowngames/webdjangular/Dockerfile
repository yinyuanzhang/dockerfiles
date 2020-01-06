### Stage 1: build ###
FROM node:12.6.0-alpine

# Set environment variables
ENV WWW_ROOT "/wwwroot"

# Set working directory.
RUN mkdir ${WWW_ROOT}
WORKDIR ${WWW_ROOT}

# Copy app dependencies.
COPY package.json ${WWW_ROOT}/

# Install app dependencies.
RUN npm install

# Copy app files.
COPY . ${WWW_ROOT}

# Build app
RUN npm run build-all:prod

# Expose the port the app runs in
EXPOSE 4000

# Serve the app
CMD ["node", "dist/server"]