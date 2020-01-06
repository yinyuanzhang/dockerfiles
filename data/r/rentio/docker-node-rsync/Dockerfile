FROM mhart/alpine-node:10

RUN apk add --no-cache curl rsync openssh git
RUN yarn config set workspaces-experimental true
RUN wget -O ./inst.tgz https://s3-eu-west-1.amazonaws.com/lokalise-assets/cli/lokalise-0.721-linux-amd64.tgz &&\
    tar -xvzf ./inst.tgz &&\
    rm -rf ./inst.tgz &&\
    mv ./lokalise /usr/local/bin/lokalise 
