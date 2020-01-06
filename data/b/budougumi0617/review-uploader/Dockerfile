FROM golang:1.12.7 AS build

WORKDIR /go/bin

RUN go get github.com/prasmussen/gdrive

FROM vvakame/review:3.1
COPY --from=build /go/bin/gdrive /bin/

CMD ["gdrive", "version"]
