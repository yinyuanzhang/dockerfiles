FROM golang:1.11 as build

RUN mkdir /app
WORKDIR /app
COPY . /app
ENV CGO_ENABLED=0

RUN go build -o sleeptime


FROM alpine as run
RUN mkdir /app
COPY --from=build /app/sleeptime /app/sleeptime
CMD /app/sleeptime
