### Stage 1: build app ###
FROM node:11.11.0-alpine as builder

# Set up working directory
RUN mkdir /app
WORKDIR /app

# Copy app dependencies file
COPY package.json package-lock.json /app/

# Install app dependencies
RUN npm install

# Copy app files
COPY . /app

# Build app
RUN npm run build -- --prod --output-path ./dist/out


### State 2: delivery app ###

FROM nginx:1.15.9-alpine

# Add support for TZ
RUN sed -i 's/dl-cdn.alpinelinux.org/mirror.tuna.tsinghua.edu.cn/g' /etc/apk/repositories
RUN apk add --update tzdata
RUN rm -rf /var/cache/apk/*

# Remove default nginx website
RUN rm -rf /usr/share/nginx/html/*


# Copy output directory from builder to nginx image
COPY --from=builder /app/dist/out /usr/share/nginx/html

# Copy nginx configuration file
COPY ./nginx/nginx.conf /etc/nginx/conf.d/default.conf
COPY ./nginx/real_ip.conf /etc/nginx/conf.d/real_ip.conf
COPY ./nginx/uwsgi_params /
