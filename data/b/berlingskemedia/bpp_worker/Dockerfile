FROM node:10.16-alpine

LABEL authors="Alexey Gorb <alexey.gorb@persgroep.net>"

# Set the working directory.
WORKDIR /worker

ADD worker /worker
ADD package.json /worker/
ADD package-lock.json /worker/
ADD rds-combined-ca-bundle.pem /worker/

RUN npm i --production

# To be using in a GET {API}/version
# https://docs.docker.com/v17.12/docker-cloud/builds/advanced/
#RUN echo $CACHE_TAG > /app/server/version
RUN echo Build date `date +%Y-%m-%d` > /worker/version

# When starting a container with our image, this command will be run.
CMD ["node", "/worker/index.js"]

