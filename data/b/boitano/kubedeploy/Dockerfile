FROM golang:1.12.5-stretch as build
WORKDIR /app
COPY * ./

ENV GOBIN /go/bin
RUN go get
RUN CGO_ENABLED=0 GOOS=linux GOARCH=amd64 go build -ldflags="-w -s" -o kubedeploy

FROM gcr.io/cloud-builders/docker as release

COPY --from=build /app/kubedeploy /bin/kubedeploy
ENTRYPOINT [ "/bin/kubedeploy" ]