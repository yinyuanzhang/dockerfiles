FROM golang AS build
WORKDIR /gophersays
COPY go.mod .
COPY go.sum .
RUN go mod download
COPY . .
RUN GOOS=linux GOARCH=amd64 go build -ldflags="-w -s" -a -o /go/bin/gophersays

FROM scratch
LABEL maintainer="d94.zaragoza@gmail.com"
COPY --from=build /go/bin/gophersays /go/bin/gophersays
ENTRYPOINT ["/go/bin/gophersays"]