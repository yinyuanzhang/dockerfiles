FROM node:latest

ENV NODE_OPTIONS --max_old_space_size=1024
ENV NG_BUILD_ARGS --prod --aot

# Create a directory where our app will be placed
RUN mkdir -p /usr/src/app

# Change directory so that our commands run inside this new directory
WORKDIR /usr/src/app

# Copy npm package files
COPY package.json package-lock.* /usr/src/app/

# Install npm dependencies
#RUN npm install --@devfactory:registry=http://nexus-rapid-proto.devfactory.com/repository/npm-proto/
RUN npm install

# Copy app files to out container
COPY . /usr/src/app

# Build app
RUN node_modules/.bin/ng build $NG_BUILD_ARGS

FROM nginx:latest

RUN mkdir -p /etc/app

COPY /docker /etc/app/package

# Copy build files from first image to nginx dir
RUN rm -rf /usr/share/nginx/html/*
COPY --from=0 /usr/src/app/dist/ /usr/share/nginx/html/

# Copying nginx config
RUN rm -f /etc/nginx/nginx.conf
RUN cp /etc/app/package/mime.types /etc/nginx/mime.types

# Expose port 80
EXPOSE 80

# Copy custom nginx.conf file and run entrypoint.sh to start nginx server
WORKDIR /etc/app
RUN chmod +x /etc/app/package/entrypoint.sh
CMD ["/etc/app/package/entrypoint.sh"]
