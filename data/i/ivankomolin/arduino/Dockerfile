FROM golang as build

RUN go get -u github.com/arduino/arduino-cli


FROM ubuntu

WORKDIR /app

COPY --from=build /go/bin/arduino-cli /usr/bin/

RUN apt-get update && \
	apt-get install -y ca-certificates picocom bash && \
	apt-get clean