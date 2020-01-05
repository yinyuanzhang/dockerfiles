FROM ubuntu:18.04

## Label(s)
## %labels
LABEL maintainer karatechop@brie.ninja

## Set up the application
## %setup
RUN mkdir /app
## %files
COPY helloworld /app

## Install what you need and no more
## %post
RUN apt-get update && \ 
    apt-get install -y --no-install-recommends \
    fortune-mod \ 
    fortunes-bofh-excuses  \
    && rm -rf /var/lib/apt/lists/*

## Configure
## %environment
ENV PATH /usr/local/bin:/usr/games:$PATH

## Go
## %runscript
CMD ["/app/helloworld" ]
