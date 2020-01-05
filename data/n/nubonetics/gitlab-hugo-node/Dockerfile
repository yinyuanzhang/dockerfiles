FROM registry.gitlab.com/pages/hugo:latest
MAINTAINER bsamadi@nubonetics.com
RUN apk update
RUN apk add --update g++ nodejs nodejs-npm go
RUN go get --tags extended  github.com/spf13/hugo
RUN hugo version
RUN npm install -g postcss-cli
RUN npm install -g autoprefixer
