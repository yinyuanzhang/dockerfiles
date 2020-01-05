FROM golang:alpine

ARG HUGO_VERSION=v0.55.4

RUN apk add --no-cache git

RUN mkdir $HOME/src \
      && cd $HOME/src \
      && git clone https://github.com/gohugoio/hugo.git \
      && cd hugo \
      && git checkout ${HUGO_VERSION} \
      && go install

RUN hugo new site /lodoc

WORKDIR /lodoc

RUN git clone https://github.com/NickolasHKraus/alabaster-2.git themes/alabaster-2

COPY config.toml .

EXPOSE 1313

ENTRYPOINT hugo serve --bind 0.0.0.0
