#########################
### build environment ###
#########################

# base image
FROM prosmartxyz/angular-cli as builder

# set working directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# add `/usr/src/app/node_modules/.bin` to $PATH
# ENV PATH /usr/src/app/node_modules/.bin:$PATH

# tells npm to not show anything about progress or anything
RUN npm set progress=false
# just copy dependencies definitions
COPY package*.json /usr/src/app/

# install npm dependencies from lock-file
RUN npm ci

# add app
COPY . /usr/src/app
# generate build
RUN npm run build

##################
### production ###
##################

# base image
FROM nginx:1.14.1-alpine

## Remove default nginx website
RUN rm -rf /usr/share/nginx/html/*

# copy artifact build from the 'build environment'
COPY --from=builder /usr/src/app/dist/hestia-app /usr/share/nginx/html

## overrides nginx defaults
COPY ./nginx-custom.conf /etc/nginx/conf.d/default.conf

# expose port 80
EXPOSE 80

# run nginx
CMD ["nginx", "-g", "daemon off;"]
