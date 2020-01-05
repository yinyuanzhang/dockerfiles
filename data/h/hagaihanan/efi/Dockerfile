FROM node:10.15.0

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

ARG NODE_ENV
ENV NODE_ENV $NODE_ENV
ARG INSTANCE_NAME
ENV INSTANCE_NAME $INSTANCE_NAME
ARG PORT=8000
ENV PORT $PORT

COPY . /usr/src/app
RUN npm install && npm link

EXPOSE $PORT

CMD [ "efi" ]
