FROM golang:latest as builder
WORKDIR /go/src/github.com/ancientlore/webnull
COPY . .
WORKDIR /go/src/github.com/ancientlore/webnull
RUN CGO_ENABLED=0 GOOS=linux GO111MODULE=on go get .
RUN CGO_ENABLED=0 GOOS=linux GO111MODULE=on go install
WORKDIR /go/foo
RUN echo "root:x:0:0:user:/home:/bin/bash" > passwd && echo "nobody:x:65534:65534:user:/home:/bin/bash" >> passwd
RUN echo "root:x:0:" > group && echo "nobody:x:65534:" >> group

FROM gcr.io/distroless/static:latest
COPY --from=builder /go/foo/group /etc/group
COPY --from=builder /go/foo/passwd /etc/passwd
COPY --from=builder /go/bin/webnull /go/bin/webnull
EXPOSE 8080
USER nobody:nobody
ENTRYPOINT ["/go/bin/webnull", "-addr", ":8080"]
