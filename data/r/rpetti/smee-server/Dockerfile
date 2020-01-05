FROM node:10-alpine as builder

LABEL name="smee-server"
LABEL version="1.0"
LABEL description="Dockerized version of smee server: https://smee.io"

RUN apk update && apk add git
WORKDIR /
RUN git clone https://github.com/probot/smee.git && cd smee && npm install --unsafe-perm

FROM node:10-slim
EXPOSE 3000
WORKDIR /smee
COPY --from=builder /smee .

ENTRYPOINT [ "npm", "start" ]
