FROM golang:1.12

RUN curl https://glide.sh/get | sh
RUN apt-get update
RUN curl -sL https://deb.nodesource.com/setup_10.x | bash -
RUN apt-get install -y nodejs
RUN npm rebuild node-sass --force
RUN npm install -g gulp-cli
RUN npm install gulp@4.0.2
RUN go get -u github.com/golang/dep/cmd/dep
RUN go get -u github.com/golangci/golangci-lint/cmd/golangci-lint
