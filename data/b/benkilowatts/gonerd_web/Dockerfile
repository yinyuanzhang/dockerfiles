# stage: 2 — the production environment
FROM mhart/alpine-node:11 as builder
RUN mkdir /code
WORKDIR /code
ADD package.json .
RUN npm i
ADD . /code
RUN npm run build

FROM mhart/alpine-node:11
RUN npm install -g serve
EXPOSE 3000
RUN mkdir build
COPY --from=builder /code/build build
CMD ["serve", "-s", "build",  "-l", "tcp://0.0.0.0:3000"]
