# To clear docker data run "docker system prune -a --volumes"

# We use node.js LTS
FROM node:lts-alpine

# Create app directory
RUN mkdir -p /usr/src/app

# Setting app directory
WORKDIR /usr/src/app

# Copy all files to the image
COPY package.json /usr/src/app

# Install all dependencies
RUN npm i

# Copy all files to the image
COPY . /usr/src/app

# Setting environments variables
ENV DYNAMO_PORT 8000
ENV DYNAMO_ENDPOINT http://localhost:${DYNAMO_PORT}
ENV PORT 8001
ENV AWS_REGION localhost
ENV AWS_ACCESS_KEY_ID=AWS_ACCESS_KEY_ID
ENV AWS_SECRET_ACCESS_KEY=AWS_SECRET_ACCESS_KEY

EXPOSE ${PORT} ${DYNAMO_PORT}

# Main command
CMD [ "npm", "start" ]
