#
# MongoDB Dockerfile
#
# https://github.com/oocoder/mongodb
#

# Pull base image.
FROM debian:jessie

RUN apt-get update && apt-get install -y \
		ca-certificates \
		curl

ENV MONGODB_VERSION 3.0.2

# Signature file keys for build 2.6        
RUN curl -SLk --ssl-allow-beast "https://hkps.pool.sks-keyservers.net/pks/lookup?op=get&search=0x857FD301" | gpg --import
# In case for a different major/minor version you can use this command instead. 
# curl -kLS "https://www.mongodb.org/static/pgp/server-$MONGODB_VERSION.asc" | gpg --import 

                
# Install MongoDB.
RUN \
    curl -kLO "https://fastdl.mongodb.org/linux/mongodb-linux-x86_64-$MONGODB_VERSION.tgz" \
    && curl -kLO "https://fastdl.mongodb.org/linux/mongodb-linux-x86_64-$MONGODB_VERSION.tgz.sig" \
    && gpg --verify mongodb-linux-x86_64-$MONGODB_VERSION.tgz.sig mongodb-linux-x86_64-$MONGODB_VERSION.tgz \
    && tar -zxvf mongodb-linux-x86_64-$MONGODB_VERSION.tgz -C /usr/local --strip-components=1 \     
    && rm -rf mongodb-linux-x86_64-$MONGODB_VERSION.tgz  mongodb-linux-x86_64-$MONGODB_VERSION.tgz.sig \
    && mkdir -p /data/db


# Define mountable directories.
VOLUME ["/data/db"]

# Define working directory.
WORKDIR /data

# Define default command.
CMD ["mongod", "--dbpath", "/data/db", "--smallfiles"]

# Expose ports.
#   - 27017: process
#   - 28017: http
EXPOSE 27017
EXPOSE 28017
