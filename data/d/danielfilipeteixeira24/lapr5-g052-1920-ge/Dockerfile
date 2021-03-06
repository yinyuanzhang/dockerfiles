
# PRODUCTION DOCKERFILE
# ---------------------
# This Dockerfile allows to build a Docker image of the NestJS application
# and based on a NodeJS 12 image. The multi-stage mechanism allows to build
# the application in a "builder" stage and then create a lightweight production
# image containing the required dependencies and the JS build files.
# 
# Dockerfile best practices
# https://docs.docker.com/develop/develop-images/dockerfile_best-practices/
# Dockerized NodeJS best practices
# https://github.com/nodejs/docker-node/blob/master/docs/BestPractices.md
# https://www.bretfisher.com/node-docker-good-defaults/
# http://goldbergyoni.com/checklist-best-practice-of-node-js-in-production/

#FROM node:12-alpine as builder

#ENV NODE_ENV build

#USER node
#WORKDIR /home/node

#COPY . /home/node

#RUN npm ci \
#    && npm run build

# ---

#FROM node:12-alpine

#ENV NODE_ENV production

#USER node
#WORKDIR /home/node

#COPY --from=builder /home/node/package*.json /home/node/
#COPY --from=builder /home/node/dist/ /home/node/dist/

#RUN npm ci

#EXPOSE 3000

#CMD ["npm", "run start"]
#CMD ["node", "dist/main.js"]


#FROM node:12-alpine
#WORKDIR /app
#COPY package*.json ./
#RUN ls \
#	&& npm install

#FROM node:12-alpine
#WORKDIR /app
#$COPY --from=0 /app .
#COPY . .



FROM node:12-alpine as builder

ENV NODE_ENV build

WORKDIR /home/root

COPY . /home/root

RUN npm ci \
    && npm run build

# ---

FROM node:12-alpine

ENV NODE_ENV production

WORKDIR /home/root

COPY --from=builder /home/root/package*.json /home/root/
COPY --from=builder /home/root/dist/ /home/root/dist/

RUN npm ci

EXPOSE 3000
CMD ["node", "dist/main.js"]
