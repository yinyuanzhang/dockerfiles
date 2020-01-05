FROM ubuntu:14.04

ENV \
  DEBIAN_FRONTEND=noninteractive \
  NODE_ENV=production

RUN \
  sed -i 's/# \(.*multiverse$\)/\1/g' /etc/apt/sources.list && \
  apt-get update && \
  apt-get install -y python build-essential && \
  apt-get install -y software-properties-common && \
  apt-get install -y curl git htop man unzip vim wget && \
  curl -sL https://deb.nodesource.com/setup_5.x | sudo -E bash - && \
  apt-get install -y nodejs && \
  rm -rf /var/lib/apt/lists/*

# Provides cached layer for node_modules
ADD package.json /tmp/package.json
RUN cd /tmp && NODE_ENV=development npm install
RUN mkdir -p /app && cp -a /tmp/node_modules /app/

# Define working directory
WORKDIR /app
ADD . /app
RUN npm run build

# Expose port
EXPOSE 8080

CMD ["npm", "start"]
