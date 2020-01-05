FROM node:8 as builder

# Create app directory
WORKDIR /usr/src/app

# Install app dependencies
# A wildcard is used to ensure both package.json AND package-lock.json are copied
# where available (npm@5+)
COPY src/package*.json ./

RUN npm install
# If you are building your code for production
# RUN npm install --only=production

FROM nginx:alpine
COPY --from=builder /usr/src/app/node_modules /usr/share/nginx/html/node_modules