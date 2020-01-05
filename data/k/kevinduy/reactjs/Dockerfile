FROM node:carbon
MAINTAINER KevinDuy<mr.kevinduy@gmail.com>

# Setup environment variables
ENV NODE_PATH=/node_modules
ENV PATH=$PATH:node_modules/.bin

# Install global packages
RUN npm install -g \
	create-react-app \
	yarn

CMD [ "node" ]

WORKDIR /app
