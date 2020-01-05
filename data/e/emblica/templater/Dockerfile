# STEP 1 build executable binary
FROM golang:alpine as builder
RUN apk --update add git
COPY . $GOPATH/src/templater/
WORKDIR $GOPATH/src/templater/

#get dependancies
#you can also use dep
RUN go get -d -v
#build the binary
#RUN go build -o /go/bin/templater
RUN CGO_ENABLED=0 GOOS=linux GOARCH=amd64 go build -a -installsuffix cgo -ldflags="-w -s" -o /go/bin/templater
# STEP 2 build a small image
# start from scratch
FROM scratch
# Copy our static executable
COPY --from=builder /etc/passwd /etc/passwd
COPY --from=builder /go/bin/templater /go/bin/templater
USER nobody
ENTRYPOINT ["/go/bin/templater"]
