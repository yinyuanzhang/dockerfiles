# https://hub.docker.com/r/starefossen/ruby-node/
FROM starefossen/ruby-node:2-10

# Will expose standard port
EXPOSE 3000

# Copy assets folder and install all dependencies
WORKDIR /usr/src/app
COPY package.json ./
COPY package-lock.json ./
COPY Gruntfile.js ./
COPY src ./src
RUN npm install -y && gem install sass

# Start assets server
CMD npm start
