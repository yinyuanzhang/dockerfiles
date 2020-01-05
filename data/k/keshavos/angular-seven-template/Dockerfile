FROM node:8

# Create a directory where our app will be placed
RUN mkdir -p /usr/src/app

# Change directory so that our commands run inside this new directory
WORKDIR /usr/src/app

# Copy dependency definitions
COPY package.json /usr/src/app
COPY package-lock.json /usr/src/app

# Install dependecies
RUN npm install

# add `/usr/src/app/node_modules/.bin` to $PATH
ENV PATH /usr/src/app/node_modules/.bin:$PATH

# Get all the code needed to run the app
COPY . /usr/src/app

# Expose the port the app runs in
EXPOSE 4200

RUN npm install -g @angular/cli

# Serve the app
#CMD ["npm", "start"]

# start app
CMD ng serve --host 0.0.0.0