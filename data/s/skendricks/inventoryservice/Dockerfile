FROM node:8-alpine

EXPOSE 3000

ARG NODE_ENV
ENV NODE_ENV ${NODE_ENV}

RUN mkdir /app
WORKDIR /app
ADD package.json package-lock.json /app/
ADD . /app

## Add the wait script to the image
ADD https://github.com/ufoscout/docker-compose-wait/releases/download/2.2.1/wait /wait
RUN chmod +x /wait

## Launch the wait tool and then your application
CMD /wait && npm run dev

