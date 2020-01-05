# Use the docker image node:9.4
FROM node:9.4

ARG PUBLIC_PATH=https://sellers-dev.mookh.xyz
ARG FRONTEND_API_HOST=https://development.mymookh.com
ARG NODE_ENV=development
ARG FACEBOOK_APP_ID
ARG FACEBOOK_APP_SECRET
ARG BASE_URL=https://development.mymookh.com

ENV PUBLIC_PATH ${PUBLIC_PATH}
ENV FRONTEND_API_HOST ${FRONTEND_API_HOST}
ENV NODE_ENV ${NODE_ENV}
ENV FACEBOOK_APP_ID ${FACEBOOK_APP_ID}
ENV FACEBOOK_APP_SECRET ${FACEBOOK_APP_SECRET}
ENV BASE_URL ${BASE_URL}

# Into which the source will be copied inside the destination container.
WORKDIR /app
# It will copy the existing files to the `/app` directory.
COPY . /app
# Run npm install
RUN npm install; exit 0

#build production
RUN npm run build; exit 0

# Start the app.
CMD npm run start:prod
# Expose the port of the app thats running in the container.
EXPOSE 3000
