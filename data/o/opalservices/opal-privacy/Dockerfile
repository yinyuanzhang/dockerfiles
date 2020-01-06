# Select source image
FROM node:stretch

# Install all dependencies
RUN apt-get update -q && apt-get upgrade -y --no-install-recommends && apt-get install -y netcat

# Install python3
RUN apt-get install -y python3-dev python3-pip
# Install python library required
RUN pip3 install git+https://github.com/OPAL-Project/codejail.git \
    && pip3 install git+https://github.com/OPAL-Project/bandicoot.git \
    && pip3 install git+https://github.com/OPAL-Project/opalalgorithms.git

# Create app directories
RUN mkdir -p /usr/app/config
WORKDIR /root

# We download the eae compute
RUN git clone -b master https://github.com/opal-project/opal-privacy

WORKDIR /root/opal-privacy

# Bundle app
RUN cp package.json /usr/app/ \
   && cp -r src /usr/app/src

WORKDIR /usr/app

# Install opal-privacy npm dependencies
RUN npm install --silent; exit 0;
RUN cat /root/.npm/_logs/*; exit 0;

EXPOSE 80
