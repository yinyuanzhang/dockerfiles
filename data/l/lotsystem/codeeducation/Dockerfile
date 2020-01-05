FROM golang:alpine as go
WORKDIR /go
COPY . .
WORKDIR /go/src/soma
RUN go build -v


FROM scratch
COPY --from=go /go/src/soma /
CMD [ "/soma" ]