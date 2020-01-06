#!/bin/bash
FROM node:10

WORKDIR /app

RUN wget https://kloudio-docker.s3-us-west-2.amazonaws.com/api/server-linux

RUN chmod 777 server-linux

CMD [ "./server-linux" ]

EXPOSE 8081
