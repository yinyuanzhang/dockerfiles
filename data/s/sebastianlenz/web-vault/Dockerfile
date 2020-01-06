FROM node:12.9.1

# Enter production mode
ENV NODE_ENV production
ENV WV_DATAPATH ''
ENV WV_SECUREPATH ''

# Install components
RUN apt-get update && apt-get -y install rsync

# Copy project files
RUN mkdir -p /usr/webvault/data
COPY . /usr/webvault

# Install dependencies
WORKDIR /usr/webvault/packages/wv-server
RUN npm install

# Run server
EXPOSE 4000
CMD ["npm", "start"]
