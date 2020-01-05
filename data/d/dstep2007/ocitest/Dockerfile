FROM node:0.12

# Install MongoDB
ENV MONGO_VERSION 3.2.1
RUN curl -SL "https://fastdl.mongodb.org/linux/mongodb-linux-x86_64-$MONGO_VERSION.tgz" | tar -xz -C /usr/local --strip-components=1

# Setup DB data volume
VOLUME /data/db

# Setup image data volume
VOLUME /data/images

# Install global npm dependencies
RUN npm install -g bower

# Create a new user
RUN useradd -ou 0 -g 0 -ms /bin/bash dev

# Copy app to the /src directory
COPY . /home/dev/src

# Install the app dependencies
RUN cd /home/dev/src; bower install --allow-root && npm install

# Set the working dir
WORKDIR /home/dev/src

EXPOSE 8080

# Start MongoDB and a terminal session on startup
ENV MONGOD_START "mongod --fork --logpath /var/log/mongodb.log --logappend --smallfiles"
#ENTRYPOINT ["/bin/sh", "-c", "$MONGOD_START && su dev && /bin/bash"]
CMD $MONGOD_START && su dev && cd /home/dev/src && node server.js
