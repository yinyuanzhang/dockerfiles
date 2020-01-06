FROM golang:1.10-alpine as builder  
RUN apk add git
RUN go get github.com/42wim/matterircd
RUN /go/bin/matterircd -version

FROM alpine:latest
RUN apk --no-cache add ca-certificates
COPY --from=0 /go/bin/matterircd /bin/matterircd
ENV MM_EXTRA_ARGS ""
CMD /bin/matterircd -bind 0.0.0.0:6667 -mmserver $MM_SERVER -mmteam $MM_TEAM $MM_EXTRA_ARGS
