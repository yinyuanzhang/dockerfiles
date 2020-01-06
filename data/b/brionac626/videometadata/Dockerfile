FROM golang:1.11.5 AS bs
LABEL maintainer="theone1632@gmail.com"

RUN apt-get update
RUN apt-get install -y libmediainfo0v5 libmediainfo-dev 
ENV GO111MODULE=on

RUN git clone https://github.com/brionac626/mediaMatedata.git
# COPY . ./mediaMatedata
RUN cd ./mediaMatedata && go build -o main

FROM ubuntu:18.04

RUN apt-get update
RUN apt-get install -y libmediainfo0v5 libmediainfo-dev 

WORKDIR /app
ENV VIDEO_DIR /video
VOLUME [ "/video" ]

COPY --from=bs /go/mediaMatedata/main /app/

ENTRYPOINT [ "./main" ]