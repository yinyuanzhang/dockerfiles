
FROM node:alpine

COPY ./build ./build

RUN npm install -g serve

ENTRYPOINT ["serve"]

CMD ["--single", "./build"]
