# base image
FROM node:lts-buster-slim


# set working directory
WORKDIR /app

# add `/app/node_modules/.bin` to $PATH
ENV PATH /app/node_modules/.bin:$PATH

# install and cache app dependencies
COPY package.json /app/package.json
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y git
RUN git --version
RUN npm install

# add app
COPY . /app

# start app
CMD ng serve --host 0.0.0.0 --disable-host-check --port 80