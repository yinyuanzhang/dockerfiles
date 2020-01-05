FROM golang
MAINTAINER bsamadi@nubonetics.com
RUN apt update
RUN apt install -y apt-utils curl gnupg2 git
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash -
RUN apt -y install nodejs
RUN npm install -g postcss-cli
RUN npm install -g autoprefixer
RUN go get --tags extended  github.com/spf13/hugo
