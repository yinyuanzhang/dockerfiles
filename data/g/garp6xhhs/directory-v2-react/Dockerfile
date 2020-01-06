# Use the docker image node:9.4
FROM node:9.4
# Into which the source will be copied inside the destination container.
WORKDIR /app
# It will copy the existing files to the `/app` directory.
COPY . /app
# Run npm install
RUN npm install; exit 0
#install cross-env
RUN npm i -g cross-env
#build dll
RUN npm run build:dll; exit 0
#build production
RUN npm run build; exit 0
#default env build
ENV NODE_ENV=development
ENV FACEBOOK_PIXEL_ID=2147425078816828
ENV BASE_URL=https://development.mymookh.com
ENV SENDY_TOKEN=g26ZBb3XVfWaAKVPrCAD
ENV SENDY_USER_NAME=mookh
# Start the app.
CMD cross-env NODE_ENV=${NODE_ENV} FACEBOOK_PIXEL_ID=${FACEBOOK_PIXEL_ID} BASE_URL=${BASE_URL} SENDY_TOKEN=${SENDY_TOKEN} SENDY_USER_NAME=${SENDY_USER_NAME} node server
# CMD npm run start:prod
# Expose the port of the app thats running in the container.
EXPOSE 3000
